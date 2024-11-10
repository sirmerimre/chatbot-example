import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# config.py
MODEL_PATH = os.getenv("MODEL_PATH")
API_KEY = os.getenv("API_KEY")
THRESHOLD = 0.40
MAX_REQUESTS = 50
TIME_WINDOW = 60