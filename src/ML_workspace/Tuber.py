import requests
import random


class Tuber(object):
    def __init__(self, ImgID: str) -> None:
        print("success")
        self.ImgID = ImgID
        self.IMAGE = requests.get(f"replti:{self.ImgID}")

    def Predict():
        """
        """
        result = random.choice([True, False])
        return result

    def __repr__(self) -> str:
        return "ALL SET"
