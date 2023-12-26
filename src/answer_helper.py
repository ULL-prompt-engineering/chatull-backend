from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
import re
import time

def answer_question(question, docs_page_content, classify_model, question_model):
    ##llm = OpenAI(model_name="text-davinci-003", temperature=0)
    llm = ChatOpenAI(
    model_name='gpt-3.5-turbo-16k',
    temperature = 0
    )

    print("Modelo cargado")
    promt_classification = PromptTemplate(
        input_variables=["question", "sections"],
        template=classify_model
    )

    promt_question = PromptTemplate(
        input_variables=["question", "section_content"],
        template=question_model
    )
    
    classification_model = LLMChain(llm=llm, prompt=promt_classification)
    question_model = LLMChain(llm=llm, prompt=promt_question)

    start_time = time.time()

    correct_section = classification_model.run(question=question, sections=docs_page_content.keys())

    correct_section = re.sub(r"\d+\.", "", correct_section)
    correct_section = re.sub(r"\n", "", correct_section)
    correct_section = re.sub(r"Respuesta:", "", correct_section)
    correct_section = re.sub(r"respuesta:", "", correct_section)
    correct_section = correct_section.strip()
    

    try:
        section_content = docs_page_content[correct_section]
    except:
        section_content = "No hay información disponible sobre la sección a la que pertenece la pregunta."


    response = question_model.run(question=question, section_content=section_content)
    end_time = time.time()

    duration = end_time - start_time

    response = re.sub(r"\;", "\n", response)

    return response, duration
        

def save_time_to_csv(question, answer, duration, csv_file_name="times.csv"):
    with open(csv_file_name, 'a') as f:
        f.write(f"{question};{answer};{duration}\n")