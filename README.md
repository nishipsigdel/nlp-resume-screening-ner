# Job Screening Resume NER Model

This repository contains trained spaCy pipelines for extracting information from English resumes. It is the model component of the *Job Recommendation and Resume Screening System Using Natural Language Processing* academic project.

The repository intentionally contains no frontend, backend, training data, or applicant resumes.

## Included models

| Directory | Purpose |
| --- | --- |
| `models/model-best` | Checkpoint selected by spaCy as the best evaluation result. Use this model for inference. |
| `models/model-last` | Final checkpoint at the end of training, retained for reproducibility and comparison. |

Both models use a `roberta-base` transformer with spaCy named-entity recognition (NER). Large transformer weights are stored with Git LFS, so clone the repository with Git LFS enabled.

## Extracted entity labels

- `College Name`
- `Companies worked at`
- `Degree`
- `Designation`
- `Email Address`
- `Graduation Year`
- `SKILL`
- `Skills`

## Setup

Requirements: Python 3.10 or newer and Git LFS.

```bash
git lfs install
git clone <YOUR_REPOSITORY_URL>
cd job-screening-spacy-model
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install the runtime packages and test the selected model:

```bash
pip install -r requirements.txt
python scripts/test_model.py
```

## Using the model

```python
from pathlib import Path
import spacy

model_path = Path("models/model-best")
nlp = spacy.load(model_path)

resume_text = "Jane Doe is a Python Developer with a BSc in Computer Science."
doc = nlp(resume_text)

for entity in doc.ents:
    print(entity.text, "->", entity.label_)
```

## Technical details

- Framework: spaCy 3.8.x and `spacy-transformers`
- Transformer: `roberta-base`
- Pipeline: `transformer`, `ner`
- Language: English (`en`)
- Training output: Google Colab

`model-best` recorded an entity F-score of 1.0 on its development split. This score reflects the data split used during training and should not be treated as a guarantee of real-world resume-screening accuracy.

## Responsible use

This model supports information extraction; it should not be the sole basis for hiring decisions. Evaluate the model for accuracy, bias, privacy, and legal compliance before using it with real candidates. Do not commit resumes, annotations, API keys, or other personal data to this public repository.
