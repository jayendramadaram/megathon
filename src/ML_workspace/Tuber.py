import requests
import random


class Tuber(object):
    def __init__(self, ImgID: str) -> None:
        self.ImgID = ImgID
        print(
            f"https://storage.jayendramadara.repl.co/download?id={self.ImgID}")
        self.IMAGE = requests.get(
            f"https://storage.jayendramadara.repl.co/download?id={self.ImgID}")

    def Predict(self):
        """
        """
        # print(self.IMAGE.text)
        result = random.choice([True, False])
        return result

    def __repr__(self) -> str:
        return "True" if self.IMAGE.status_code else "False"
