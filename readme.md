Requirements:

- openai
- python-dotenv

jersey_analyzer/
│────src
│ ├── main.py # Entry point, handles menu & workflow
│ ├── config.py # Loads ENV (API key, prompt, paths)
│ ├── processor.py # Core logic (OpenAI calls, parsing, file moves)
│ ├── excel_writer.py # Handles Excel writing/appending
│ ├── logger.py # Centralized logging (success, error logs)
│ ├── utils.py # Helpers (timestamp, folder creation, etc.)
│── jersey_prompt.txt # Prompt template (editable without touching code)
│── logs/ #error logs
│── images/
│ ├── not_process/ # Input images
│ ├── success/ # Processed successfully
│ ├── error/ # Parsing/AI issues

🍏 Step-by-Step Setup (macOS)

1. Install Homebrew

Open Terminal and run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

After install, add brew to your shell config:

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

Check:

brew --version

2. Install pyenv
   brew install pyenv

Add pyenv to shell (zsh):

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

Check:

pyenv --version

3. Install Python via pyenv

Choose a stable version (example: 3.11.9):

pyenv install 3.11.9
pyenv local 3.11.9

Verify:

python --version

# Python 3.11.9
