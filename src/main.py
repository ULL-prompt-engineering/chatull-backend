from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from subjects import subjects, sections, subjects_promp_classify, subjects_promp_question
from subjects_helper import buildSections
from answer_helper import answer_question, save_time_to_csv
from regulation import regulation, regulation_sections, regulation_promp_classify, regulation_promp_question
import uuid

import threading
import time

documents = buildSections(subjects, sections)
regulation_docs = buildSections(regulation, regulation_sections)

api_keys = {}
api_key_control = {}

app = Flask(__name__)

CORS(app)

def print_api_keys():
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()), api_keys)
        time.sleep(15)

t = threading.Thread(target=print_api_keys)
t.start()

@app.route('/set_api_key', methods=['POST'])
def set_api_key():
    # Extraer la API key y el token de sesión desde la solicitud
    api_key = request.json.get('api_key')

    if api_key is None:
        return make_response("API key no encontrada", 400)
    
    session_token = ""
    if api_key_control.get(api_key) is not None:
        session_token = api_key_control.get(api_key)
        # update ip
        api_keys[session_token]["ip"] = request.remote_addr
    else:
        session_token = str(uuid.uuid4())
        request_ip = request.remote_addr
        api_keys[session_token] = {"api_key": api_key, "ip": request_ip}
        api_key_control[api_key] = session_token

    response = make_response(jsonify({'message': 'API key guardada exitosamente', 'session_token': session_token}), 200)
    return response

@app.route('/get_answer/<session_token>', methods=['GET'])
def get_answer(session_token):
    question = request.args.get('question')  # Obtener la pregunta de los parámetros de la URL
    subject = request.args.get('subject')  # Obtener la pregunta de los parámetros de la URL
    if question is None:
        return make_response("Pregunta no encontrada", 400)
    if subject is None:
        return make_response("Materia no encontrada", 400)

    session = api_keys.get(session_token)
    if session is None:
        return make_response("Sesión no encontrada", 401)
    
    if session.get("ip") != request.remote_addr:
        return make_response("Datos de sesión inválidos", 401)
    
    api_key = session.get("api_key")

    docs_page_content = documents[subjects[subject]]
    answer, duration = answer_question(question, docs_page_content, subjects_promp_classify, subjects_promp_question, api_key)
    answer = answer.replace("\n", "<br>")
    save_time_to_csv(question, answer, duration)
    return jsonify({"answer": answer})

@app.route('/get_teacher_answer/<session_token>', methods=['GET'])
def get_teacher_answer(session_token):
    question = request.args.get('question')  # Obtener la pregunta de los parámetros de la URL
    if question is None:
        return make_response("Pregunta no encontrada", 400)
    
    session = api_keys.get(session_token)
    if session is None:
        return make_response("Sesión no encontrada", 401)
    
    if session.get("ip") != request.remote_addr:
        return make_response("Datos de sesión inválidos", 401)
    
    api_key = session.get("api_key")
    
    regulation_name = list(regulation.values())[0]
    regulation_page_content = regulation_docs[regulation_name]
    answer, duration = answer_question(question, regulation_page_content, regulation_promp_classify, regulation_promp_question, api_key)
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