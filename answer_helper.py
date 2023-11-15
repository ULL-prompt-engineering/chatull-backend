from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
import re

def answer_question(question, docs_page_content):
    llm = OpenAI(model_name="text-davinci-003", temperature=0)

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
            Eres un modelo de lenguaje experto en responder preguntas sobre una sección de una guía académica de una asignatura de la ULL.
            Solo debes buscar información en la información que se te proporciona y responder a la pregunta.

            Si en algún momento consideras que no puedes responder a la pregunta, debes responder "No se la respuesta".

            La información del tipo (ejemplo): 
                Última modificación: 26-06-2023
                Aprobación: 10-07-2023
                Página 4 de 13
            
            puedes ignorla a la hora de buscar información, ya que la información proporcionada es continua y no se encuentra en una sola página.

            Información: {section_content}

            Pregunta: {question}

            Da respuesta a la pregunta de la mejor forma posible, es decir siendo lo más preciso y conciso posible.
            """
    )
    
    classification_model = LLMChain(llm=llm, prompt=promt_classification)
    question_model = LLMChain(llm=llm, prompt=promt_question)
    correct_section = classification_model.run(question=question, sections=docs_page_content.keys())

    correct_section = re.sub(r"\d+\.", "", correct_section)
    correct_section = re.sub(r"\n", "", correct_section)
    correct_section = correct_section.strip()
    

    section_content = docs_page_content[correct_section]

    response = question_model.run(question=question, section_content=section_content)

    return response
