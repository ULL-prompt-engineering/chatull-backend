from openai import OpenAI

import re
import time

# Esta función se encarga de responder a una pregunta dada, primero clasificando la pregunta en una sección de la documentación y luego respondiendo a la pregunta en base a la sección encontrada.
def answer_question(question, docs_page_content, classify_model, question_model, classify_description, api_key):
    client = OpenAI(api_key=api_key)

    start_time = time.time()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": classify_model.format(question=question, sections="".join(docs_page_content.keys()), description=classify_description)}
        ]
    )
    
    correct_section = completion.choices[0].message.content

    correct_section = re.sub(r"\d+\.", "", correct_section)
    correct_section = re.sub(r"\n", "", correct_section)
    correct_section = re.sub(r"Respuesta:", "", correct_section)
    correct_section = re.sub(r"respuesta:", "", correct_section)
    correct_section = re.sub(r"\,", "", correct_section)
    correct_section = re.sub(r'"', "", correct_section)
    correct_section = correct_section.strip()
    

    try:
        section_content = docs_page_content[correct_section]
    except:
        section_content = "No hay información disponible, prueba a preguntar de otra manera."
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question_model.format(question=question, section_content=section_content)},
        ]
    )
    response = completion.choices[0].message.content
    end_time = time.time()

    duration = end_time - start_time

    response = re.sub(r"\;", "\n", response)

    return response, duration
        
# Esta función se encarga de guardar el tiempo de respuesta junto con la pregunta y la respuesta en un archivo csv.
def save_time_to_csv(question, answer, duration, csv_file_name="times.csv"):
    with open(csv_file_name, 'a') as f:
        f.write(f"{question};{answer};{duration};{time.time()}\n")


# Esta función se encarga de verificar si una API key es válida o no.
def check_api_key(api_key):
    client = OpenAI(api_key=api_key)
    try:
        client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Prueba de API key"}
            ]
        )
        return True
    except:
        return False