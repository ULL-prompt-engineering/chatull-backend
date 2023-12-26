from flask import Flask, jsonify, request  # Añadir 'request' para obtener los datos de la pregunta
from flask_cors import CORS
from dotenv import load_dotenv
from subjects import subjects, sections, subjects_promp_classify, subjects_promp_question
from subjects_helper import buildSections
from answer_helper import answer_question, save_time_to_csv
from regulation import regulation, regulation_sections, regulation_promp_classify, regulation_promp_question

load_dotenv()
documents = buildSections(subjects, sections)
regulation_docs = buildSections(regulation, regulation_sections)

app = Flask(__name__)

CORS(app)

@app.route('/get_answer', methods=['GET'])
def get_answer():
    question = request.args.get('question')  # Obtener la pregunta de los parámetros de la URL
    subject = request.args.get('subject')  # Obtener la pregunta de los parámetros de la URL
    docs_page_content = documents[subjects[subject]]
    answer, duration = answer_question(question, docs_page_content, subjects_promp_classify, subjects_promp_question)
    answer = answer.replace("\n", "<br>")
    save_time_to_csv(question, answer, duration)
    return jsonify({"answer": answer})
@app.route('/get_teacher_answer', methods=['GET'])
def get_teacher_answer():
    question = request.args.get('question')  # Obtener la pregunta de los parámetros de la URL
    print(question)
    regulation_name = list(regulation.values())[0]
    regulation_page_content = regulation_docs[regulation_name]
    answer, duration = answer_question(question, regulation_page_content, regulation_promp_classify, regulation_promp_question)
    answer = answer.replace("\n", "<br>")
    save_time_to_csv(question, answer, duration)
    return jsonify({"answer": answer})
@app.route('/documents', methods=['GET'])
def get_documents():
    response_data = []
    for subject in subjects:
        response_data.append({
            "name": subject
        })
    response_data.append({
        "name": list(regulation.keys())[0]
    })
    response = jsonify(response_data)
    return response
    
if __name__ == '__main__':
    app.run(debug=True)
