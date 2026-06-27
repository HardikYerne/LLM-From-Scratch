from pathlib import Path


class DataLoader:

    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)

    def load_documents(self):

        documents = []

        print("\nSearching in:")
        print(self.dataset_path)

        if not self.dataset_path.exists():
            print("Dataset folder does not exist.")
            return documents

        files = list(self.dataset_path.glob("*.txt"))

        print(f"Found {len(files)} text files.")

        for file_path in files:

            print("Reading:", file_path.name)

            with open(file_path, "r", encoding="utf-8") as file:

                documents.append(
                    {
                        "document_name": file_path.name,
                        "text": file.read()
                    }
                )

        return documents