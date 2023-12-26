subjects = {
    "Procesadores del Lenguaje": "PL",
    "Interfaces Inteligentes": "II",
    "Robótica Computacional": "RC",
}

sections = [
    "Datos descriptivos de la asignatura",
    "Requisitos de matrícula y calificación",
    "Profesorado que imparte la asignatura",
    "Contextualización de la asignatura en el plan de estudio",
    "Competencias",
    "Contenidos de la asignatura",
    "Metodología y volumen de trabajo del estudiante",
    "Bibliografía / Recursos",
    "Sistema de evaluación y calificación",
    "Resultados de Aprendizaje",
    "Cronograma / calendario de la asignatura"
]

subjects_promp_classify = """
           Eres un modelo de lenguaje experto en clasificar preguntas en función de la sección a la que pertenecen.
           Solo te limitaras a dar el nombre de la sección a la que pertenece la pregunt, sin más.
    
            Ejemplo: Yo: Que cosas tengo que aprobar con un 5
            Tu: 9. Sistema de evaluación y calificación
    
            Secciones: {sections}

            Pregunta: {question}

            Clasifica la pregunta en una de las secciones anteriores.
        """

subjects_promp_question = """
            Eres un modelo de lenguaje especializado en proporcionar respuestas precisas sobre información académica. La información actual es la siguiente:

            {section_content}

            Pregunta: {question}

           
            Utiliza tu capacidad para buscar información de manera inteligente y proporciona respuestas concisas basadas en el contenido suministrado. Evita respuestas extensas y la invención de datos.

            """
            
