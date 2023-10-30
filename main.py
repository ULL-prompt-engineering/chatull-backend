from flask import Flask, jsonify, request  # Añadir 'request' para obtener los datos de la pregunta
from flask_cors import CORS

from answer_helper import answer_question

app = Flask(__name__)

CORS(app)

@app.route('/get_answer', methods=['GET'])
def get_answer():
    question = request.args.get('question')  # Obtener la pregunta de los parámetros de la URL
    answer = answer_question(question)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
