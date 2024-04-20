from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from subjects import sections, subjects_promp_classify, subjects_promp_question, subjects_description
from subjects_helper import buildSections, buildSubjects
from answer_helper import answer_question, save_time_to_csv, check_api_key
from regulation import regulation, regulation_sections, regulation_promp_classify, regulation_promp_question, regulation_description
import jwt

subjects = buildSubjects()
documents = buildSections(subjects, sections, "pdf_sub")
regulation_docs = buildSections(regulation, regulation_sections, "pdf_reg")

app = Flask(__name__)
CORS(app)

# Clave secreta para firmar los tokens JWT (pon una muy complicada)
SECRET_KEY = "T,F4n*C$R5xjT+n"

# Decorador para verificar y decodificar el token JWT
def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token de autenticación faltante'}), 401
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            kwargs['api_key'] = payload['api_key']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401
        
        return func(*args, **kwargs)
    
    return wrapper

@app.route('/set_api_key', methods=['POST'])
def set_api_key():
    api_key = request.json.get('api_key')
    if api_key is None:
        return make_response("API key no encontrada", 400)
    
    if not check_api_key(api_key):
        return make_response("API key inválida", 401)

    # Genera el token JWT
    token = jwt.encode({'api_key': api_key}, SECRET_KEY, algorithm='HS256')
    
    response = make_response(jsonify({'message': 'API key guardada exitosamente', 'jwt': token}), 200)
    return response

@app.route('/get_answer', methods=['GET'], endpoint='get_answer_endpoint')
@token_required
def get_answer(api_key):
    question = request.args.get('question')
    subject = request.args.get('subject')
    if question is None or subject is None:
        return jsonify({'error': 'Pregunta o materia no encontrada'}), 400

    docs_page_content = documents.get(subject)
    if not docs_page_content:
        return jsonify({'error': 'Materia no encontrada'}), 404
    
    answer, duration = answer_question(question, docs_page_content, subjects_promp_classify, subjects_promp_question, subjects_description, api_key)
    answer = answer.replace("\n", "<br>")
    save_time_to_csv(question, answer, duration)
    return jsonify({"answer": answer})

@app.route('/get_regulation_answer', methods=['GET'], endpoint='get_regulation_answer_endpoint')
@token_required
def get_regulation_answer(api_key):
    question = request.args.get('question')
    if question is None:
        return jsonify({'error': 'Pregunta no encontrada'}), 400
    
    regulation_name = list(regulation.keys())[0]
    regulation_page_content = regulation_docs.get(regulation_name)
    if not regulation_page_content:
        return jsonify({'error': 'Regulación no encontrada'}), 404
    
    answer, duration = answer_question(question, regulation_page_content, regulation_promp_classify, regulation_promp_question, regulation_description, api_key)
    answer = answer.replace("\n", "<br>")
    save_time_to_csv(question, answer, duration)
    return jsonify({"answer": answer})

@app.route('/documents', methods=['GET'])
def get_documents():
    response_data = [{"name": subject} for subject in subjects] + [{"name": list(regulation.keys())[0]}]
    return jsonify(response_data)

@app.route('/logs', methods=['GET'])
def get_logs():
    with open("times.csv", 'r') as f:
        logs = f.readlines()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
