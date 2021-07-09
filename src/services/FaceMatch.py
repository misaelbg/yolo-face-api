class FaceMatch:

    def __init__(self, weight:str) -> None:
        self.model = self.load_model(weight)