import re

class TestCleanner:

    def clran(self,text):

        text =re.sub(r"\s+"," ",text)


        text = text.strip()

        return text