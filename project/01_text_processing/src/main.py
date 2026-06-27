from pathlib import Path
from data_loader import DataLoader
from analyzer import CorpusAnalyzer


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

    loader = DataLoader(dataset_path)

    documents = loader.load_documents()

    print("Documents Loaded :", len(documents))

    for document in documents:
        print(document["document_name"])

    print("=" * 60)

    if len(documents) == 0:
        print("ERROR : No documents found.")
        return

    analyzer = CorpusAnalyzer(documents)

    stats = analyzer.analyze()

    print("\n")
    print("=" * 50)
    print("LLM FROM SCRATCH")
    print("Project 01 : Text Processing")
    print("=" * 50)

    print(f"Documents Loaded : {stats['documents']}")
    print(f"Total Sentences : {stats['sentences']}")
    print(f"Total Words : {stats['words']}")
    print(f"Total Characters : {stats['characters']}")
    print(f"Average Words/Document : {stats['average_words']}")
    print(f"Longest Document : {stats['longest_document']}")


if __name__ == "__main__":
    main()