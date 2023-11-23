## Setup and execution

Add a `.env` file with the following content:

``` bash
OPENAI_API_KEY=<your key>
```

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

Now go to <https://chatull.pages.dev/> and fill a question.

```
¿Cuales son los horarios de tutoría del profesor Casiano?
```

It works fine:

```
El profesor Casiano ofrece tutorías los lunes de 9:30 a 12:30 en el Módulo C de la Escuela Superior de Ingeniería y Tecnología (AN.4A ESIT) en el despacho P2.106, los martes de 10:30 a 11:30 en el Módulo A de la Escuela Superior de Ingeniería y Tecnología (AN.4A ESIT) en el despacho P2.037, y los jueves de 9:30 a 12:30 en el Módulo C de la Escuela Superior de Ingeniería y Tecnología (AN.4A ESIT) en el despacho P2.106.
```

## References

* About .pkl files: <https://docs.python.org/3/library/pickle.html>
* How to Create Requirements.txt Python?: <https://www.scaler.com/topics/how-to-create-requirements-txt-python/>
