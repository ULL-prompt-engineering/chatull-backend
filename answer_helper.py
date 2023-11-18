from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
import re

def answer_question(question, docs_page_content):
    ##llm = OpenAI(model_name="text-davinci-003", temperature=0)
    llm = ChatOpenAI(
    model_name='gpt-3.5-turbo-16k',
    temperature = 0
    )

    print("Modelo cargado")
    promt_classification = PromptTemplate(
        input_variables=["question", "sections"],
        template="""
           Eres un modelo de lenguaje experto en clasificar preguntas en función de la sección a la que pertenecen.
           Solo te limitaras a dar el nombre de la sección a la que pertenece la pregunt, sin más.
    
            Ejemplo: Yo: Que cosas tengo que aprobar con un 5
            Tu: 9. Sistema de evaluación y calificación
    
            Secciones: {sections}

            Pregunta: {question}

            Clasifica la pregunta en una de las secciones anteriores.
        """
    )

    promt_question = PromptTemplate(
        input_variables=["question", "section_content"],
        template="""
            Eres un modelo de lenguaje especializado en proporcionar respuestas precisas sobre información académica. La información actual es la siguiente:

            {section_content}

            Pregunta: {question}

           
            Utiliza tu capacidad para buscar información de manera inteligente y proporciona respuestas concisas basadas en el contenido suministrado. Evita respuestas extensas y la invención de datos.

            """
    )
    
    classification_model = LLMChain(llm=llm, prompt=promt_classification)
    question_model = LLMChain(llm=llm, prompt=promt_question)
    correct_section = classification_model.run(question=question, sections=docs_page_content.keys())

    correct_section = re.sub(r"\d+\.", "", correct_section)
    correct_section = re.sub(r"\n", "", correct_section)
    correct_section = re.sub(r"Respuesta:", "", correct_section)
    correct_section = re.sub(r"respuesta:", "", correct_section)
    correct_section = correct_section.strip()
    

    section_content = docs_page_content[correct_section]

    with open("section_content.txt", "a") as f:
        f.write(section_content)

    response = question_model.run(question=question, section_content=section_content)

    response = re.sub(r"\;", "\n", response)

    return response
