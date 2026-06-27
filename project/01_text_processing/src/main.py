from pathlib import Path

from data_loader import DataLoader
from analyzer import CorpusAnalyzer
from cleaner import TextCleaner
from normalizer import TextNormalizer
from writer import CorpusWriter


def main():

    # ======================================================
    # Project Paths
    # ======================================================

    project_root = Path(__file__).resolve().parents[3]

    raw_dataset_path = project_root / "datasets" / "raw"

    processed_dataset_path = project_root / "datasets" / "processed"

    # ======================================================
    # Load Dataset
    # ======================================================

    print("=" * 60)
    print("LLM FROM SCRATCH")
    print("PROJECT 01 : TEXT PROCESSING")
    print("=" * 60)

    loader = DataLoader(raw_dataset_path)

    documents = loader.load_documents()

    if len(documents) == 0:
        print("No documents found.")
        return

    print(f"\nDocuments Loaded : {len(documents)}")

    for document in documents:
        print(f"✓ {document['document_name']}")

    # ======================================================
    # Text Cleaning
    # ======================================================

    cleaner = TextCleaner()

    for document in documents:
        document["text"] = cleaner.clean(document["text"])

    print("\nText Cleaning Completed.")

    # ======================================================
    # Text Normalization
    # ======================================================

    normalizer = TextNormalizer()

    for document in documents:
        document["text"] = normalizer.normalize(document["text"])

    print("Text Normalization Completed.")

    # ======================================================
    # Corpus Analysis
    # ======================================================

    analyzer = CorpusAnalyzer(documents)

    stats = analyzer.analyze()

    print("\nCorpus Analysis Completed.")

    # ======================================================
    # Save Processed Dataset
    # ======================================================

    writer = CorpusWriter(processed_dataset_path)

    writer.save_documents(documents)

    writer.save_statistics(stats)

    # ======================================================
    # Final Report
    # ======================================================

    print("\n" + "=" * 60)
    print("PROJECT REPORT")
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