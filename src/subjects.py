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
           Solo te limitaras a dar el nombre de la sección a la que pertenece la pregunta, sin más.
    
            Ejemplo: Yo: Que horarios de tutoria tiene israel
            Tu: Profesorado que imparte la asignatura
    
            Secciones: {sections}

            Pregunta: {question}

            Clasifica la pregunta en una de las secciones anteriores. Es importante que no añadas nada más a la respuesta. Tienes que dar la sección exacta tal y como aparece en la lista.
        """

subjects_promp_question = """
            Eres un modelo de lenguaje especializado en proporcionar respuestas precisas sobre información académica. La información actual es la siguiente:

            {section_content}

            Pregunta: {question}

           
            Utiliza tu capacidad para buscar información de manera inteligente y proporciona respuestas concisas basadas en el contenido suministrado. Evita respuestas extensas. Siempre dalas bien estructuradas y con un formato adecuado.
            Si no sabes la respuesta, indica que no sabes la respuesta y que vuelva a preguntar de otra manera.
            Ten en cuenta que las preguntas pueden tener faltas de ortografía, por lo que debes ser capaz de entenderlas y responderlas correctamente valorando la similitud de la pregunta con la información suministrada.
            """
            
