from data_loader import DataLoader
from analyzer import CorpusAnalyzer
from pathlib import Path


def main():

    project_root = Path(__file__).resolve().parents[2]
    dataset_path = project_root / "datasets" / "raw"

    loader = DataLoader(dataset_path)
    documents = loader.load_documents()

    analyzer = CorpusAnalyzer(documents)

    stats = analyzer.analyze()

    print("=" * 50)
    print("LLM FROM SCRATCH")
    print("Project 01 : Text Processing")
    print("=" * 50)

    print(f"\nDocuments Loaded : {stats['documents']}")
    print(f"Total Sentences : {stats['sentences']}")
    print(f"Total Words : {stats['words']}")
    print(f"Total Characters : {stats['characters']}")
    print(f"Average Words/Document : {stats['average_words']}")
    print(f"Longest Document : {stats['longest_document']}")


if __name__ == "__main__":
    main()