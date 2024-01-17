from openai import OpenAI

import os
import re
import time

def answer_question(question, docs_page_content, classify_model, question_model):
    client = OpenAI()

    start_time = time.time()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": classify_model.format(question=question, sections="".join(docs_page_content.keys()))},
        ]
    )
    
    correct_section = completion.choices[0].message.content

    correct_section = re.sub(r"\d+\.", "", correct_section)
    correct_section = re.sub(r"\n", "", correct_section)
    correct_section = re.sub(r"Respuesta:", "", correct_section)
    correct_section = re.sub(r"respuesta:", "", correct_section)
    correct_section = correct_section.strip()
    

    try:
        section_content = docs_page_content[correct_section]
    except:
        section_content = "No hay información disponible sobre la sección a la que pertenece la pregunta."

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
        

def save_time_to_csv(question, answer, duration, csv_file_name="times.csv"):
    with open(csv_file_name, 'a') as f:
        f.write(f"{question};{answer};{duration}\n")