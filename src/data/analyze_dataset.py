
import json
from pathlib import Path
from collections import Counter

cleaned_path = Path("data/processed/education_dataset_cleaned.jsonl")
splits_dir = Path("data/splits")
report_path = Path("reports/dataset_report.md")


def load_jsonl(file_path):
    records = []

    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            records.append(json.loads(line))

    return records


cleaned_records = load_jsonl(cleaned_path)

train_records = load_jsonl(splits_dir / "train.jsonl")
validation_records = load_jsonl(splits_dir / "validation.jsonl")
test_records = load_jsonl(splits_dir / "test.jsonl")

topic_counts = Counter(
    record["topic"] for record in cleaned_records
)

difficulty_counts = Counter(
    record["difficulty"] for record in cleaned_records
)

question_type_counts = Counter(
    record["question_type"] for record in cleaned_records
)

total_records = len(cleaned_records)

split_total = (
    len(train_records)
    + len(validation_records)
    + len(test_records)
)

report = []

report.append("# Educational Dataset Analysis Report")
report.append("")
report.append("## 1. Dataset Overview")
report.append("")
report.append(f"- Total cleaned records: {total_records}")
report.append(f"- Training records: {len(train_records)}")
report.append(f"- Validation records: {len(validation_records)}")
report.append(f"- Testing records: {len(test_records)}")
report.append(f"- Total records across splits: {split_total}")
report.append("")

report.append("## 2. Subject Distribution")
report.append("")
for topic, count in sorted(topic_counts.items()):
    report.append(f"- {topic}: {count}")

report.append("")

report.append("## 3. Difficulty Distribution")
report.append("")
for difficulty, count in sorted(difficulty_counts.items()):
    report.append(f"- {difficulty}: {count}")

report.append("")

report.append("## 4. Question Type Distribution")
report.append("")
for question_type, count in sorted(question_type_counts.items()):
    report.append(f"- {question_type}: {count}")

report.append("")

report.append("## 5. Dataset Split Distribution")
report.append("")
report.append("| Dataset | Records | Percentage |")
report.append("|---|---:|---:|")

for name, records in [
    ("Training", train_records),
    ("Validation", validation_records),
    ("Testing", test_records)
]:
    percentage = (
        len(records) / total_records * 100
        if total_records > 0 else 0
    )
    report.append(
        f"| {name} | {len(records)} | {percentage:.2f}% |"
    )

report.append("")

report.append("## 6. Dataset Quality Checks")
report.append("")

if split_total == total_records:
    report.append("- Split count check: Passed")
else:
    report.append("- Split count check: Failed")

if total_records == 0:
    report.append("- Dataset availability: Failed")
else:
    report.append("- Dataset availability: Passed")

report.append("")

report.append("## 7. Observations")
report.append("")
report.append(
    f"- The current dataset contains {total_records} cleaned records."
)
report.append(
    "- The dataset covers multiple educational topics and question types."
)
report.append(
    "- The current dataset is an initial sample and must be expanded "
    "towards the target of 1,000 records."
)
report.append(
    "- The small dataset size is not sufficient for reliable model "
    "fine-tuning or final performance evaluation."
)

report_path.parent.mkdir(parents=True, exist_ok=True)

report_path.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("\n--- Dataset Analysis ---")
print("Total cleaned records:", total_records)

print("\nSubject Distribution:")
for topic, count in sorted(topic_counts.items()):
    print(f"{topic}: {count}")

print("\nDifficulty Distribution:")
for difficulty, count in sorted(difficulty_counts.items()):
    print(f"{difficulty}: {count}")

print("\nQuestion Type Distribution:")
for question_type, count in sorted(question_type_counts.items()):
    print(f"{question_type}: {count}")

print("\nSplit Distribution:")
print("Training:", len(train_records))
print("Validation:", len(validation_records))
print("Testing:", len(test_records))

print("\nSplit count check:", "Passed" if split_total == total_records else "Failed")
print("Report saved to:", report_path)
