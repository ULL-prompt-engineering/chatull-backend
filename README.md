Add a `.env` file with the following content:

``` bash
OPENAI_API_KEY=<your key>
```

Install dependencies:

``` bash
# Create virtual environment
python3 -m venv ./.venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install langchain openai==0.28.1 python-dotenv flask flask-cors  PyPDF2 tiktoken 
```

Warning: There were problems with `faiss-gpu`. Dependence retired for now. 

Start the server:

```
(.venv) ➜  chatull-backend git:(master) ✗ python main.py 
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 691-027-428
```

Now go to <https://chatull.pages.dev/> and fill a question.

It gives an error:

```
27.0.0.1 - - [19/Nov/2023 10:25:10] "GET /get_answer?question=¿cuales%20son%20los%20horarios%20de%20tutoría?&subject=Procesadores%20del%20Lenguaje HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/Users/casianorodriguezleon/campus-virtual/2324/tfg2324/gabriel-jonay-vera-estevez/chatull-backend/.venv/lib/python3.11/site-packages/langchain/vectorstores/faiss.py", line 53, in dependable_faiss_import
    import faiss
ModuleNotFoundError: No module named 'faiss'
```