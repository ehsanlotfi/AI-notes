Step-by-Step Knowledge Distillation with Hugging Face

1. Install Required Libraries
```
!pip install transformers datasets evaluate torch -q
```

2. Import Dependencies
```
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
)

from datasets import load_dataset
import evaluate
import numpy as np
from tqdm import tqdm

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")
```

3. Load the Dataset
In this example, we use the SST-2 sentiment classification dataset.
```
dataset = load_dataset("sst2")
print(dataset["train"][0])
```

4. Define Teacher and Student Models
```
# Teacher model
TEACHER_MODEL = "textattack/bert-base-uncased-SST-2"

# Student model
STUDENT_MODEL = "google/mobilebert-uncased"

NUM_LABELS = 2
MAX_LENGTH = 128
BATCH_SIZE = 32
```

5. Load the Tokenizer and Models
```
# Shared tokenizer (using the teacher tokenizer)
tokenizer = AutoTokenizer.from_pretrained(TEACHER_MODEL)

# Pretrained teacher model
teacher = AutoModelForSequenceClassification.from_pretrained(
    TEACHER_MODEL,
    num_labels=NUM_LABELS
).to(device)

teacher.eval()  # Teacher is only used for inference

# Student model to be trained
student = AutoModelForSequenceClassification.from_pretrained(
    STUDENT_MODEL,
    num_labels=NUM_LABELS
).to(device)

print(f"Teacher params: {sum(p.numel() for p in teacher.parameters()):,}")
print(f"Student params: {sum(p.numel() for p in student.parameters()):,}")
```

6. Preprocess the Dataset
```
def preprocess(examples):
    return tokenizer(
        examples["sentence"],
        truncation=True,
        max_length=MAX_LENGTH,
    )

tokenized = dataset.map(preprocess, batched=True)

tokenized = tokenized.remove_columns(["sentence", "idx"])
tokenized = tokenized.rename_column("label", "labels")
tokenized.set_format("torch")

# Dynamic padding
collator = DataCollatorWithPadding(tokenizer=tokenizer)

train_loader = DataLoader(
    tokenized["train"],
    batch_size=BATCH_SIZE,
    shuffle=True,
    collate_fn=collator
)

val_loader = DataLoader(
    tokenized["validation"],
    batch_size=BATCH_SIZE,
    collate_fn=collator
)

print(f"Train batches: {len(train_loader)}")
print(f"Validation batches: {len(val_loader)}")
```

7. Define the Distillation Loss Function
This loss combines:
KL-Divergence loss for transferring knowledge from the teacher
Cross-Entropy loss using the original labels
```
def distillation_loss(
    student_logits,
    teacher_logits,
    true_labels,
    temperature=4.0,
    alpha=0.7
):
    """
    alpha:
        Weight assigned to the KD loss

    1 - alpha:
        Weight assigned to the standard CE loss

    temperature:
        Softens the probability distribution
    """

    # Teacher soft targets
    soft_teacher = F.softmax(teacher_logits / temperature, dim=-1)

    # Student predictions
    soft_student = F.log_softmax(student_logits / temperature, dim=-1)

    # Knowledge Distillation loss
    kd_loss = F.kl_div(
        soft_student,
        soft_teacher,
        reduction="batchmean"
    ) * (temperature ** 2)

    # Standard classification loss
    ce_loss = F.cross_entropy(student_logits, true_labels)

    # Final combined loss
    total_loss = alpha * kd_loss + (1 - alpha) * ce_loss

    return total_loss, kd_loss.item(), ce_loss.item()
```

8. Training Loop
```
EPOCHS = 3
LEARNING_RATE = 2e-5
TEMPERATURE = 4.0
ALPHA = 0.7

optimizer = torch.optim.AdamW(
    student.parameters(),
    lr=LEARNING_RATE
)

# Learning rate scheduler
total_steps = len(train_loader) * EPOCHS

scheduler = torch.optim.lr_scheduler.LinearLR(
    optimizer,
    start_factor=1.0,
    end_factor=0.1,
    total_iters=total_steps
)

def train_one_epoch(epoch):

    student.train()
    total_loss = 0

    loop = tqdm(
        train_loader,
        desc=f"Epoch {epoch+1}/{EPOCHS}"
    )

    for batch in loop:

        batch = {
            k: v.to(device)
            for k, v in batch.items()
        }

        labels = batch["labels"]

        # Teacher inference without gradients
        with torch.no_grad():
            teacher_out = teacher(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"]
            )

        # Student forward pass
        student_out = student(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"]
        )

        # Compute loss
        loss, kd_l, ce_l = distillation_loss(
            student_out.logits,
            teacher_out.logits,
            labels,
            temperature=TEMPERATURE,
            alpha=ALPHA
        )

        optimizer.zero_grad()

        loss.backward()

        torch.nn.utils.clip_grad_norm_(
            student.parameters(),
            1.0
        )

        optimizer.step()
        scheduler.step()

        total_loss += loss.item()

        loop.set_postfix(
            loss=loss.item(),
            kd=kd_l,
            ce=ce_l
        )

    return total_loss / len(train_loader)
```

9. Evaluation Loop
```
metric = evaluate.load("accuracy")

def evaluate_model(model, loader, model_name="Model"):

    model.eval()

    all_preds = []
    all_labels = []

    with torch.no_grad():

        for batch in loader:

            batch = {
                k: v.to(device)
                for k, v in batch.items()
            }

            outputs = model(**batch)

            preds = torch.argmax(
                outputs.logits,
                dim=-1
            )

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(
                batch["labels"].cpu().numpy()
            )

    acc = metric.compute(
        predictions=all_preds,
        references=all_labels
    )

    print(f"{model_name} Accuracy: {acc['accuracy']:.4f}")

    return acc["accuracy"]
```

10.  Run the Full Distillation Process
```
print("=" * 50)
print("Evaluating Teacher Model Before Training")

teacher_acc = evaluate_model(
    teacher,
    val_loader,
    "Teacher"
)

print("\nEvaluating Student Model Before Training")

student_acc_before = evaluate_model(
    student,
    val_loader,
    "Student (Before Training)"
)

print("=" * 50)
print("Starting Knowledge Distillation")
print("=" * 50)

history = []

for epoch in range(EPOCHS):

    avg_loss = train_one_epoch(epoch)

    val_acc = evaluate_model(
        student,
        val_loader,
        f"Student Epoch {epoch+1}"
    )

    history.append({
        "epoch": epoch + 1,
        "loss": avg_loss,
        "val_acc": val_acc
    })

    print(f"Average Loss: {avg_loss:.4f}\n")
```

11.  Compare Final Results
```
print("\n" + "=" * 50)
print("Final Comparison")
print("=" * 50)

teacher_acc = evaluate_model(
    teacher,
    val_loader,
    "Teacher (BERT-base)"
)

student_acc = evaluate_model(
    student,
    val_loader,
    "Student (MobileBERT)"
)

teacher_params = sum(
    p.numel() for p in teacher.parameters()
)

student_params = sum(
    p.numel() for p in student.parameters()
)

print(f"\nTeacher Parameters: {teacher_params:,}")
print(f"Student Parameters: {student_params:,}")

print(
    f"Compression Ratio: "
    f"{teacher_params / student_params:.2f}x"
)

print(f"Teacher Accuracy: {teacher_acc:.4f}")
print(f"Student Accuracy: {student_acc:.4f}")

print(
    f"Accuracy Difference: "
    f"{abs(teacher_acc - student_acc):.4f}"
)
```

12.  Save the Distilled Student Model
```
student.save_pretrained("./student_distilled")

tokenizer.save_pretrained("./student_distilled")

print(
    "Student model saved successfully "
    "to: ./student_distilled"
)
```

13.  Test the Distilled Model
```
from transformers import pipeline

# Load the saved student model
clf = pipeline(
    "text-classification",
    model="./student_distilled",
    tokenizer="./student_distilled",
    device=0 if torch.cuda.is_available() else -1
)

# Test samples
samples = [
    "This movie was absolutely amazing!",
    "The film was boring and too long.",
    "I really enjoyed the storyline.",
    "Terrible acting, waste of time."
]

print("Test Results:")

for text in samples:

    result = clf(text)[0]

    label = (
        "Positive"
        if result["label"] == "LABEL_1"
        else "Negative"
    )

    print(
        f"'{text}'\n"
        f"→ {label} "
        f"(score: {result['score']:.3f})\n"
    )
```


| Component       | Description                                                   |
|----------------|---------------------------------------------------------------|
| Teacher Model  | Fine-tuned BERT-base trained on SST-2                         |
| Student Model  | Lightweight MobileBERT model                                  |
| Loss Function  | Combination of KL-Divergence and Cross-Entropy                |
| Temperature    | Softens probability distributions for knowledge transfer      |
| Alpha          | Balances KD loss and label-based loss                         |