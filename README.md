``` bash
# Create virtual environment
python3 -m .venv ./.venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install langchain openai python-dotenv flask flask-cors faiss-gpu PyPDF2 tiktoken
```