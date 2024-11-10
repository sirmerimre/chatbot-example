from transformers import pipeline
from config import MODEL_PATH, THRESHOLD
from logger import Logger
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d")
filename = f"classification_results_{timestamp}.json"
logger = Logger(file_path= filename)

class Classifier:
    def __init__(self):
        # Load zero-shot classification pipeline with a pre-trained model
        self.classifier = pipeline("zero-shot-classification", model=MODEL_PATH)
        self.candidate_labels = [
            "travel_insurance",
            "travel_policy",
            "exclusions",
            "claims_process",
            "cancellation",
            "excess_covered",
            # "excess_covered_travel_insurance",
            "coronavirus"
        ]

    def classify(self, user_query):
        result = self.classifier(user_query, self.candidate_labels, multi_label=True)
        # Filter results to match only predefined candidate labels

        valid_results = [
            {"label": label, "score": score } for label, score in zip(result['labels'], result['scores'])
            if label in self.candidate_labels and score >= THRESHOLD
        ]

        logger.log(result, user_query, valid_results)
        return valid_results
