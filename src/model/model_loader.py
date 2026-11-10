
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
MODEL_ID = "google/gemma-3-1b-it"

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

print("Tokenizer loaded successfully!")

print("Loading SLM model...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32
)

model.to("cpu")
model.eval()

print("Model loaded successfully!")

def generate_answer(question: str) -> str:

    messages = [
        {
            "role": "system",
            "content": "You are a helpful education assistant. Explain concepts in simple English."
        },
        {
            "role": "user",
            "content": question
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_tokens = outputs[0][inputs["input_ids"].shape[1]:]

    answer = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    return answer


if __name__ == "__main__":

    question = "What is Artificial Intelligence?"

    print("\nStudent Question:", question)

    answer = generate_answer(question)

    print("\nSLM Answer:", answer)
