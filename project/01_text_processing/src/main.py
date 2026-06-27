from pathlib import Path

from data_loader import DataLoader
from analyzer import CorpusAnalyzer
from cleaner import TextCleaner
from normalizer import TextNormalizer


def main():

    # Project Root
    project_root = Path(__file__).resolve().parents[3]

    # Dataset Path
    dataset_path = project_root / "datasets" / "raw"

    print("=" * 60)
    print("DEBUG INFORMATION")
    print("=" * 60)

    print("Current File :", Path(__file__).resolve())
    print("Project Root :", project_root)
    print("Dataset Path :", dataset_path)
    print("Dataset Exists :", dataset_path.exists())

    # -----------------------------
    # Load Dataset
    # -----------------------------
    loader = DataLoader(dataset_path)
    documents = loader.load_documents()

    print(f"\nDocuments Loaded : {len(documents)}")

    for document in documents:
        print(f"- {document['document_name']}")

    if len(documents) == 0:
        print("\nERROR : No documents found.")
        return

    # -----------------------------
    # Clean & Normalize
    # -----------------------------
    cleaner = TextCleaner()
    normalizer = TextNormalizer()

    for document in documents:

        text = document["text"]

        text = cleaner.clean(text)
        text = normalizer.normalize(text)

        document["text"] = text

    print("\nText Cleaning Completed.")
    print("Text Normalization Completed.")

    # -----------------------------
    # Analyze Corpus
    # -----------------------------
    analyzer = CorpusAnalyzer(documents)
    stats = analyzer.analyze()

    # -----------------------------
    # Print Statistics
    # -----------------------------
    print("\n" + "=" * 60)
    print("LLM FROM SCRATCH")
    print("Project 01 : Text Processing")
    print("=" * 60)

    print(f"Documents           : {stats['documents']}")
    print(f"Sentences           : {stats['sentences']}")
    print(f"Words               : {stats['words']}")
    print(f"Characters          : {stats['characters']}")
    print(f"Average Words/Doc   : {stats['average_words']}")
    print(f"Longest Document    : {stats['longest_document']}")

    print("=" * 60)
    print("Project 01 Completed Successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()