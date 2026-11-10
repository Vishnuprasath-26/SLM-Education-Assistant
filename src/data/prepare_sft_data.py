import json
from pathlib import Path

INPUT_DIR = Path("data/splits")
OUTPUT_DIR = Path("data/adaptation")

SPLITS = {
    "train.jsonl": "sft_train.jsonl",
    "validation.jsonl": "sft_validation.jsonl",
    "test.jsonl": "sft_test.jsonl"
}


def load_jsonl(file_path):
    records = []

    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                records.append(json.loads(line))

    return records


def convert_to_sft_format(record):

    user_prompt = (
        "You are an educational assistant. "
        "Explain concepts using simple English.\n\n"
        f"Topic: {record['topic']}\n"
        f"Difficulty: {record['difficulty']}\n"
        f"Question: {record['question']}"
    )

    return {
        "id": record["id"],
        "topic": record["topic"],
        "difficulty": record["difficulty"],
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            },
            {
                "role": "assistant",
                "content": record["answer"]
            }
        ]
    }


def main():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_records = 0

    for input_name, output_name in SPLITS.items():

        input_path = INPUT_DIR / input_name
        output_path = OUTPUT_DIR / output_name

        records = load_jsonl(input_path)

        converted_records = [
            convert_to_sft_format(record)
            for record in records
        ]

        with output_path.open("w", encoding="utf-8") as file:

            for record in converted_records:
                file.write(
                    json.dumps(record, ensure_ascii=False) + "\n"
                )

        total_records += len(converted_records)

        print(f"{output_name}: {len(converted_records)} records")

    print("\nSFT dataset preparation completed!")
    print("Total records:", total_records)
    print("Output directory:", OUTPUT_DIR)


if __name__ == "__main__":
    main()