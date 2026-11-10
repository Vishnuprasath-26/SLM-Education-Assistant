
import json
from pathlib import Path

dataset = [
    {
        "id": 1,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is Python?",
        "answer": "Python is a high-level, general-purpose programming language known for its readable syntax.",
        "source": "Original educational content"
    },
    {
        "id": 2,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Explanation",
        "question": "What is a variable in Python?",
        "answer": "A variable is a name that refers to a value stored in a Python program.",
        "source": "Original educational content"
    },
    {
        "id": 3,
        "topic": "Artificial Intelligence",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is Artificial Intelligence?",
        "answer": "Artificial Intelligence is a field of computer science that develops systems capable of performing tasks that normally require human intelligence.",
        "source": "Original educational content"
    },
    {
        "id": 4,
        "topic": "Artificial Intelligence",
        "difficulty": "Intermediate",
        "question_type": "Example-based",
        "question": "Give three real-life applications of Artificial Intelligence.",
        "answer": "Examples include voice assistants that understand spoken commands, recommendation systems that suggest content, and systems that help detect objects in images.",
        "source": "Original educational content"
    },
    {
        "id": 5,
        "topic": "Machine Learning",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is Machine Learning?",
        "answer": "Machine Learning is a field of AI in which computer systems learn patterns from data to make predictions or decisions.",
        "source": "Original educational content"
    },
    {
        "id": 6,
        "topic": "Machine Learning",
        "difficulty": "Intermediate",
        "question_type": "Comparison",
        "question": "What is the difference between supervised and unsupervised learning?",
        "answer": "Supervised learning uses labeled training data, while unsupervised learning finds patterns in data without provided labels.",
        "source": "Original educational content"
    },
    {
        "id": 7,
        "topic": "Deep Learning",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is Deep Learning?",
        "answer": "Deep Learning is a branch of Machine Learning that uses neural networks with multiple layers to learn patterns from data.",
        "source": "Original educational content"
    },
    {
        "id": 8,
        "topic": "Deep Learning",
        "difficulty": "Intermediate",
        "question_type": "Explanation",
        "question": "What is an artificial neural network?",
        "answer": "An artificial neural network is a computing model made of interconnected units called neurons that process information and learn patterns.",
        "source": "Original educational content"
    },
    {
        "id": 9,
        "topic": "Generative AI",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is Generative AI?",
        "answer": "Generative AI is a type of AI that creates new content such as text, images, audio or code based on learned patterns.",
        "source": "Original educational content"
    },
    {
        "id": 10,
        "topic": "Generative AI",
        "difficulty": "Intermediate",
        "question_type": "Explanation",
        "question": "What is a prompt in Generative AI?",
        "answer": "A prompt is an instruction or input given to a generative AI model to guide the content it produces.",
        "source": "Original educational content"
    },
    {
        "id": 11,
        "topic": "Small Language Models",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is a Small Language Model?",
        "answer": "A Small Language Model is a relatively compact language model designed to perform language tasks with fewer computational resources than larger models.",
        "source": "Original educational content"
    },
    {
        "id": 12,
        "topic": "Small Language Models",
        "difficulty": "Intermediate",
        "question_type": "Comparison",
        "question": "What is one difference between an SLM and an LLM?",
        "answer": "An SLM generally has fewer parameters and lower resource requirements, while an LLM is generally larger and may support a broader range of tasks.",
        "source": "Original educational content"
    },
    {
        "id": 13,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is a Python list?",
        "answer": "A list is an ordered, mutable collection that can store multiple values in Python.",
        "source": "Original educational content"
    },
    {
        "id": 14,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is a Python tuple?",
        "answer": "A tuple is an ordered collection of values that cannot be changed after creation.",
        "source": "Original educational content"
    },
    {
        "id": 15,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Explanation",
        "question": "What is the difference between a list and a tuple?",
        "answer": "A list is mutable, meaning its elements can be changed. A tuple is immutable, meaning its elements cannot be changed after creation.",
        "source": "Original educational content"
    },
    {
        "id": 16,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Definition",
        "question": "What is a Python dictionary?",
        "answer": "A dictionary is a collection that stores data as key-value pairs.",
        "source": "Original educational content"
    },
    {
        "id": 17,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Explanation",
        "question": "What is a Python function?",
        "answer": "A function is a reusable block of code designed to perform a particular task.",
        "source": "Original educational content"
    },
    {
        "id": 18,
        "topic": "Python",
        "difficulty": "Beginner",
        "question_type": "Example-based",
        "question": "How do you define a function in Python?",
        "answer": "Use the def keyword followed by the function name and parentheses. For example: def greet(): print('Hello').",
        "source": "Original educational content"
    },
    {
        "id": 19,
        "topic": "Python",
        "difficulty": "Intermediate",
        "question_type": "Explanation",
        "question": "What is a Python loop?",
        "answer": "A loop repeatedly executes a block of code. Python provides for loops and while loops.",
        "source": "Original educational content"
    },
    {
        "id": 20,
        "topic": "Python",
        "difficulty": "Intermediate",
        "question_type": "Comparison",
        "question": "What is the difference between a for loop and a while loop?",
        "answer": "A for loop commonly iterates over a sequence or iterable, while a while loop repeats as long as its condition remains true.",
        "source": "Original educational content"
    },
    {
        "id": 21,
        "topic": "Python",
        "difficulty": "Intermediate",
        "question_type": "Definition",
        "question": "What is exception handling in Python?",
        "answer": "Exception handling allows a program to respond to runtime errors using constructs such as try, except, else, and finally.",
        "source": "Original educational content"
    },
    {
        "id": 22,
        "topic": "Python",
        "difficulty": "Intermediate",
        "question_type": "Example-based",
        "question": "How can you handle division by zero in Python?",
        "answer": "Use a try-except block to catch ZeroDivisionError and handle it without unexpectedly stopping the program.",
        "source": "Original educational content"
    }
]

output_path = Path("data/raw/education_dataset.jsonl")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    for record in dataset:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")

print("Dataset collection completed!")
print("Total records:", len(dataset))
print("Saved file:", output_path)
