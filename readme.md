# Jersey Analyzer

A tiny CLI tool to analyze jersey images using OpenAI and log the results to Excel.

## Requirements

- `openai`
- `python-dotenv`

> _Optional:_ If you write `.xlsx`, add `openpyxl`. You may also use `pandas`.

---

## Project Structure
jersey_analyzer/
├─ src/
│ ├─ main.py # Entry point: menu & workflow
│ ├─ config.py # Loads ENV (API key, prompt, paths)
│ ├─ processor.py # Core logic (OpenAI calls, parsing, file moves)
│ ├─ excel_writer.py # Handles Excel writing/appending
│ ├─ logger.py # Centralized logging (success, error logs)
│ └─ utils.py # Helpers (timestamp, folder creation, etc.)
├─ jersey_prompt.txt # Prompt template (editable without touching code)
├─ logs/ # Error/success logs
└─ images/
├─ not_process/ # Input images
├─ success/ # Processed successfully
└─ error/ # Parsing/AI issues
