from data_loader import DataLoader


def main():

    loader = DataLoader(r"C:\Users\hardi\OneDrive\Desktop\LLM-From-Scratch\datasets\raw")

    documents = loader.load_documents()

    print("=" * 50)
    print("LLM FROM SCRATCH")
    print("Project 01 : Text Processing")
    print("=" * 50)

    print(f"\nDocuments Loaded : {len(documents)}\n")

    for index, document in enumerate(documents, start=1):
        print(f"{index}. {document['document_name']}")

    print("\nCorpus Successfully Created")


if __name__ == "__main__":
    main()