## Setup and execution

If you don't already have an OpenAI account, navigate to the [OpenAI website](https://www.openai.com/).

Here, you will see a "Sign Up" button at the top right corner of the website. Click on it and fill in your details to create an account. You can sign up with your GitHub or Google accounts. After signing up, you'll receive an email from OpenAI to confirm your account. Open this email and click on the verification link. This step helps to ensure the security of your account.

After logging in, in the top right corner of your screen you'll see an icon with your account name. Click it to open the dropdown menu then click "View API keys".

Now you're in the API keys section, you should see a button "Create new secret key". Click on that button to generate a new API key. Name your key. You will see your secret key that has been generated. Copy your secret key.

Add a `.env` file with the following content:

``` bash
OPENAI_API_KEY=<your key>
```
Paste your key there.

You can use the `.env.example` file as a template, remember to change the name to `.env`.

Install dependencies:

``` bash
# Create virtual environment
python3 -m venv ./.venv

# Activate virtual environment
source .venv/bin/activate
```

Install dependencies

```
pip install langchain openai==0.28.1 python-dotenv flask flask-cors PyPDF2 
```

Start the server:

```
(.venv) ➜  chatull-backend git:(master) ✗ python src/main.py 
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 691-027-428
```

Now go to the [Frontend Repo](https://github.com/ULL-prompt-engineering/chatull-frontend) and clone the repository.

Then execute the following commands;
```bash
cd chatull-frontend
npm install
npm run dev
```
And go to http://localhost:4321/

Once you get into, go to chat page and test fill a question.

¿Cuales son los horarios de tutoría del profesor Casiano?
```

It works fine:

```
El profesor Casiano ofrece tutorías los lunes de 9:30 a 12:30 en el Módulo C de la Escuela Superior de Ingeniería y Tecnología (AN.4A ESIT) en el despacho P2.106, los martes de 10:30 a 11:30 en el Módulo A de la Escuela Superior de Ingeniería y Tecnología (AN.4A ESIT) en el despacho P2.037, y los jueves de 9:30 a 12:30 en el Módulo C de la Escuela Superior de Ingeniería y Tecnología (AN.4A ESIT) en el despacho P2.106.
```

## References

* About .pkl files: <https://docs.python.org/3/library/pickle.html>
* How to Create Requirements.txt Python?: <https://www.scaler.com/topics/how-to-create-requirements-txt-python/>
