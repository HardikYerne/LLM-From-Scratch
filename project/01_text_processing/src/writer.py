from pathlib import Path
import json


class CorpusWriter:

    def __init__(self, output_path):
        self.output_path = Path(output_path)

        # Create folder if it doesn't exist
        self.output_path.mkdir(parents=True, exist_ok=True)

    def save_documents(self, documents):

        for document in documents:

            file_path = self.output_path / document["document_name"]

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(document["text"])

        print(f"\nSaved {len(documents)} processed documents.")

    def save_statistics(self, statistics):

        file_path = self.output_path / "statistics.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(statistics, file, indent=4)

        print("Statistics saved successfully.")