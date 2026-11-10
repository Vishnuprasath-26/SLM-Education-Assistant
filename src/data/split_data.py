
import json
import random
from pathlib import Path

input_path = Path("data/processed/education_dataset_cleaned.jsonl")
output_dir = Path("data/splits")

random_seed = 42

records = []

with input_path.open("r", encoding="utf-8") as file:
    for line in file:
        record = json.loads(line)
        records.append(record)

random_generator = random.Random(random_seed)
random_generator.shuffle(records)

total_records = len(records)

train_size = int(total_records * 0.70)
validation_size = int(total_records * 0.15)

train_records = records[:train_size]

validation_records = records[
    train_size:train_size + validation_size
]

test_records = records[
    train_size + validation_size:
]

output_dir.mkdir(parents=True, exist_ok=True)

datasets = {
    "train.jsonl": train_records,
    "validation.jsonl": validation_records,
    "test.jsonl": test_records
}

for filename, dataset in datasets.items():
    output_path = output_dir / filename

    with output_path.open("w", encoding="utf-8") as file:
        for record in dataset:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"{filename}: {len(dataset)} records")

print("\nDataset splitting completed!")
print("Total records:", total_records)
print("Random seed:", random_seed)
