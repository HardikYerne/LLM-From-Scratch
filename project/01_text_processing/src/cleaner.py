import re


class TextCleaner:

    def clean(self, text):

        # Remove extra spaces, tabs and newlines
        text = re.sub(r"\s+", " ", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text