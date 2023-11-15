from flask import Flask, jsonify, request  # Añadir 'request' para obtener los datos de la pregunta
from flask_cors import CORS
from dotenv import load_dotenv
from subjects import subjects, sections
from subjects_helper import buildSubjectsSections
from answer_helper import answer_question

load_dotenv()
documents = buildSubjectsSections(subjects, sections)

app = Flask(__name__)

CORS(app)

@app.route('/get_answer', methods=['GET'])
def get_answer():
    question = request.args.get('question')  # Obtener la pregunta de los parámetros de la URL
    subject = request.args.get('subject')  # Obtener la pregunta de los parámetros de la URL
    docs_page_content = documents[subjects[subject]]
    answer = answer_question(question, docs_page_content)
    print(answer)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
