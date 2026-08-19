from pathlib import Path

import spacy


def main() -> None:
    model_path = Path(__file__).resolve().parents[1] / "models" / "model-best"
    nlp = spacy.load(model_path)

    sample_resume = (
        "Aarav Sharma is a Software Engineer at Example Technologies. "
        "He holds a Bachelor of Science in Computer Science and has skills in Python and SQL. "
        "Contact: aarav@example.com."
    )
    doc = nlp(sample_resume)

    print(f"Loaded pipeline: {nlp.pipe_names}")
    print("Recognized entities:")
    for entity in doc.ents:
        print(f"- {entity.text} ({entity.label_})")


if __name__ == "__main__":
    main()
