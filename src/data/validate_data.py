
import json
from pathlib import Path
from collections import Counter

input_path = Path("data/raw/education_dataset.jsonl")
output_path = Path("data/processed/education_dataset_cleaned.jsonl")

required_fields = [
    "id",
    "topic",
    "difficulty",
    "question_type",
    "question",
    "answer",
    "source"
]

text_fields = [
    "topic",
    "difficulty",
    "question_type",
    "question",
    "answer",
    "source"
]

valid_difficulties = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

valid_records = []
errors = []

with input_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):

        try:
            record = json.loads(line)

            if not isinstance(record, dict):
                errors.append(
                    f"Line {line_number}: Record must be a JSON object."
                )
                continue

            record_valid = True

            for field in required_fields:
                if field not in record:
                    errors.append(
                        f"Line {line_number}: Missing field '{field}'."
                    )
                    record_valid = False

            if "id" in record:
                if type(record["id"]) is not int or record["id"] <= 0:
                    errors.append(
                        f"Line {line_number}: ID must be a positive integer."
                    )
                    record_valid = False

            for field in text_fields:
                if field in record:
                    if not isinstance(record[field], str) or not record[field].strip():
                        errors.append(
                            f"Line {line_number}: Field '{field}' must contain text."
                        )
                        record_valid = False

            if (
                isinstance(record.get("difficulty"), str)
                and record["difficulty"] not in valid_difficulties
            ):
                errors.append(
                    f"Line {line_number}: Invalid difficulty."
                )
                record_valid = False

            if record_valid:
                valid_records.append((line_number, record))

        except json.JSONDecodeError:
            errors.append(
                f"Line {line_number}: Invalid JSON format."
            )

ids = [record["id"] for _, record in valid_records]

questions = [
    record["question"].strip().lower()
    for _, record in valid_records
]

duplicate_ids = [
    item for item, count in Counter(ids).items()
    if count > 1
]

duplicate_questions = [
    item for item, count in Counter(questions).items()
    if count > 1
]

duplicate_id_set = set(duplicate_ids)
duplicate_question_set = set(duplicate_questions)

cleaned_records = []

for line_number, record in valid_records:

    question = record["question"].strip().lower()

    is_duplicate = False

    if record["id"] in duplicate_id_set:
        errors.append(
            f"Line {line_number}: Duplicate ID {record['id']}."
        )
        is_duplicate = True

    if question in duplicate_question_set:
        errors.append(
            f"Line {line_number}: Duplicate question."
        )
        is_duplicate = True

    if not is_duplicate:
        cleaned_records.append(record)

output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    for record in cleaned_records:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")

print("\n--- Dataset Validation Report ---")
print("Total valid records before duplicate removal:", len(valid_records))
print("Total cleaned records:", len(cleaned_records))
print("Total errors:", len(errors))
print("Duplicate IDs:", duplicate_ids)
print("Duplicate questions:", duplicate_questions)
print("Cleaned dataset saved to:", output_path)

if errors:
    print("\nValidation Errors:")
    for error in errors:
        print("-", error)

if not errors and not duplicate_ids and not duplicate_questions:
    print("\nDataset validation successful!")
else:
    print("\nDataset cleaning completed with issues. Review the errors.")
