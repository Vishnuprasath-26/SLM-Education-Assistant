# SLM Education Assistant



## 1\. Project Overview



The SLM Education Assistant is an educational question-answering application powered by a Small Language Model (SLM).



The application uses Gemma 3 1B through Ollama to answer educational questions in simple English.



It covers six major educational domains:



* Python
* Artificial Intelligence
* Machine Learning
* Deep Learning
* Generative AI
* Small Language Models



The project explores model research, dataset preparation, baseline evaluation, inference optimization, model adaptation feasibility, and API deployment.



## 2\. Project Objectives



The main objectives are:



1\. Research and compare different Small Language Models.

2\. Prepare and validate an educational question-answering dataset.

3\. Evaluate the selected model using baseline experiments.

4\. Investigate LoRA-based model adaptation.

5\. Optimize inference performance through prompt engineering and output token control.

6\. Compare baseline and optimized model performance.

7\. Deploy the selected model through a FastAPI application.

8\. Test API endpoints and document the project results.



## 3\. Key Features



* Educational question answering.
* Simple English responses.
* Gemma 3 1B model integration.
* Ollama-based local inference.
* Prompt optimization.
* Baseline and optimized performance evaluation.
* FastAPI REST API.
* Input validation using Pydantic.
* Error handling and application logging.
* Automated API and service tests.





## 2\. Technology Stack



| Technology | Purpose |

|---|---|

| Python 3.12 | Main programming language |

| Gemma 3 1B | Small Language Model |

| Ollama | Local model inference |

| FastAPI | REST API development |

| Pydantic | Request and response validation |

| Requests | Communication with Ollama API |

| PyTorch | Deep learning framework |

| Transformers | Model loading and training framework |

| PEFT | Parameter-efficient fine-tuning investigation |

| NumPy | Numerical operations |

| Pandas | Data processing |

| Scikit-learn | Machine learning utilities |

| Pytest | Automated testing |

| HTTPX | API testing |



## 3\. Project Architecture



The application follows this workflow:



1\. User submits an educational question.

2\. FastAPI receives the request.

3\. Pydantic validates the input.

4\. The API service prepares the optimized prompt.

5\. Ollama sends the prompt to Gemma 3 1B.

6\. The model generates an answer.

7\. FastAPI returns the response to the user.

8\. Application logs record the request and processing status.





## 4\. Model Evaluation Results



The selected Gemma 3 1B model was evaluated using 10 educational questions.



### Baseline Evaluation



| Metric | Result |

|---|---:|

| Total Questions | 10 |

| Quality Score | 65/80 |

| Quality Percentage | 81.25% |

| Average Response Time | 14.342 seconds |

| Average Tokens per Second | 18.09 |

| Average Generated Tokens | 169.5 |



### Optimized Evaluation



Prompt engineering and output token control were applied to improve response performance.



| Metric | Result |

|---|---:|

| Total Questions | 10 |

| Quality Score | 72/80 |

| Quality Percentage | 90% |

| Average Response Time | 10.21 seconds |

| Average Tokens per Second | 19.53 |

| Average Generated Tokens | 119.9 |



### Performance Improvement



| Metric | Improvement |

|---|---:|

| Response Time | 28.81% faster |

| Generation Speed | 7.96% higher |

| Quality Score | +8.75 percentage points |



Note: Quality scores were assigned through manual evaluation. Results are based on a small test set of 10 questions and should be treated as preliminary.





## 5. Installation and Setup



### Prerequisites



- Python 3.12

- Ollama

- Gemma 3 1B model



### Step 1: Clone the Repository



```bash

git clone <your-repository-url>

cd SLM-Education-Assistant

```



### Step 2: Create a Virtual Environment



```powershell

python -m venv .venv

```



### Step 3: Activate the Virtual Environment



```powershell

.venv\\Scripts\\Activate.ps1

```



### Step 4: Install Dependencies



```powershell

pip install -r requirements.txt

```



### Step 5: Download the Model



```powershell

ollama pull gemma3:1b

```



### Step 6: Start Ollama



Make sure the Ollama application or server is running.



### Step 7: Start the FastAPI Application



```powershell

python -m uvicorn src.api.main:app --host 127.0.0.1 --port 8000

```



### Step 8: Open API Documentation



Visit:



http://127.0.0.1:8000/docs


## 6. API Endpoints

The application provides the following REST API endpoints.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check application availability |
| GET | `/health` | Check API health |
| POST | `/api/v1/chat` | Submit an educational question |

### Chat API Example

**Endpoint:**

`POST /api/v1/chat`

**Request Body:**

```json
{
  "question": "What is Machine Learning?"
}
```

**Response:**

The API returns a generated answer from Gemma 3 1B.

### API Documentation

FastAPI Swagger UI:

`http://127.0.0.1:8000/docs`


## 7. Testing

The project uses Pytest and HTTPX for automated API and service testing.

Run all tests from the project root:

```powershell
python -m pytest tests/ -v
```

### Test Coverage

The API module achieved 100% statement coverage.

Test results:

- Total test cases: 11
- Passed: 11
- Failed: 0

Note: The reported 100% coverage applies to the `src.api` module, not the entire project.


## 8. Project Limitations

The current project has the following limitations:

1. **Small Dataset:** The educational dataset currently contains 22 records, which is below the original target of 1,000 records.

2. **Limited Evaluation:** Model performance was evaluated using only 10 questions. Quality scores were assigned manually.

3. **No Actual Fine-tuning:** LoRA adaptation was investigated and documented, but training was not executed because of hardware limitations.

4. **Hardware Constraints:** The experiments were conducted on a CPU-based system without CUDA GPU support.

5. **Local Deployment:** The FastAPI application and Ollama model run locally. Cloud or production deployment has not been completed.

## 9. Future Improvements

- Expand the educational dataset to at least 1,000 records.
- Include more advanced and technical questions.
- Perform LoRA fine-tuning on suitable GPU hardware.
- Increase the evaluation dataset.
- Explore additional inference optimization techniques.
- Evaluate the application with real users.
- Consider cloud deployment.


## 10. Project Structure

```text
SLM-Education-Assistant/
│
├── configs/
│   ├── baseline_config.json
│   ├── optimized_config.json
│   └── adaptation_config.json
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── splits/
│   ├── adaptation/
│   └── evaluation/
│
├── logs/
│
├── reports/
│   ├── model_selection.md
│   ├── dataset_report.md
│   ├── baseline_evaluation_report.md
│   ├── adaptation_feasibility.md
│   ├── adaptation_experiment.md
│   └── optimization_report.md
│
├── src/
│   ├── api/
│   ├── data/
│   ├── evaluation/
│   ├── model/
│   └── optimization/
│
├── tests/
│   ├── test_api.py
│   └── test_services.py
│
├── .gitignore
├── README.md
└── requirements.txt
```
