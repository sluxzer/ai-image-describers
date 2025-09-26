import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# API & Prompt
API_KEY = os.getenv("OPENAI_API_KEY")

# Prompt priority: file first, then env
PROMPT_AI = None
prompt_file = os.getenv("AI_PROMPT_FILE")
if prompt_file and os.path.exists(prompt_file):
    with open(prompt_file, "r", encoding="utf-8") as f:
        PROMPT_AI = f.read()
else:
    PROMPT_AI = os.getenv("AI_PROMPT", "")

# Directories
BASE_DIR = "images"
NOT_PROCESS_DIR = os.path.join(BASE_DIR, "not_process")
SUCCESS_DIR = os.path.join(BASE_DIR, "success")
ERROR_DIR = os.path.join(BASE_DIR, "error")
LOG_DIR = "logs"

# Ensure directories exist
os.makedirs(NOT_PROCESS_DIR, exist_ok=True)
os.makedirs(SUCCESS_DIR, exist_ok=True)
os.makedirs(ERROR_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# CSV/Excel setup
EXCEL_FILE = "jersey_analysis.xlsx"
FIELDNAMES = [
    "Image Filename",
    "Description",
    "Full AI Output",
    "Created At"
]
