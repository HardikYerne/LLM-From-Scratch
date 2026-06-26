class CorpusAnalyzer:

    def __init__(self, documents):
        self.documents = documents

    def analyze(self):

        total_documents = len(self.documents)

        total_sentences = 0
        total_words = 0
        total_characters = 0

        longest_document = ""
        longest_length = 0

        for document in self.documents:

            text = document["text"]

            # Count sentences
            sentences = [s for s in text.split(".") if s.strip()]
            total_sentences += len(sentences)

            # Count words
            words = text.split()
            total_words += len(words)

            # Count characters
            total_characters += len(text)

            # Find longest document
            if len(words) > longest_length:
                longest_length = len(words)
                longest_document = document["document_name"]

        average_words = total_words / total_documents

        return {
            "documents": total_documents,
            "sentences": total_sentences,
            "words": total_words,
            "characters": total_characters,
            "average_words": round(average_words, 2),
            "longest_document": longest_document,
        }