import json
import os
from datetime import datetime

class Logger:
    def __init__(self, file_path="classification_results.json"):
        """
        Initializes the logger with the path to the log file.

        :param file_path: Path to the log file (default is "classification_results.json").
        """
        self.file_path = file_path

    def log(self, results, query, valid_results):
        """
        Log the classification results to a local file with a timestamp.

        :param valid_results:
        :param results: Classification results to log (labels and scores).
        :param query: The user query being classified.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d")
        log_entry = {
            "timestamp": timestamp,
            "query": query,
            "results": results,
            "valid_results": valid_results
        }

        # Check if the file exists, if not, create it
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([log_entry], f, indent=4)
        else:
            # Append the new log entry to the existing file
            with open(self.file_path, 'r+') as f:
                data = json.load(f)
                data.append(log_entry)
                f.seek(0)
                json.dump(data, f, indent=4)

