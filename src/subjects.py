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
           Tienes que dar la sección exacta tal y como aparece en la lista, no añadas puntos, comas, etc, la respuesta debe ser exacta.
           Si añades algo más a la respuesta, el sistema no será capaz de entenderlo y no funcionará correctamente, así que ten cuidado.
    
            Ejemplo: Yo: Que horarios de tutoria tiene israel
            Tu: Profesorado que imparte la asignatura
    
            Secciones: {sections}

            Descripcción de las secciones para ayudarte a clasificar la pregunta: {description}

            Pregunta: {question}

            Clasifica la pregunta en una de las secciones anteriores. Es importante que no añadas nada más a la respuesta.
        """

subjects_description = """
    - "Datos descriptivos de la asignatura": Información general sobre la asignatura, como nombre, código, créditos, etc.
    - "Requisitos de matrícula y calificación": Condiciones necesarias para matricularse y los criterios de evaluación.
    - "Profesorado que imparte la asignatura": Detalles sobre los profesores encargados de la asignatura, como nombre, correo electrónico, horarios de tutoría, etc.
    - "Contextualización de la asignatura en el plan de estudio": Relación de la asignatura con el plan de estudios.
    - "Competencias": Habilidades y conocimientos que se esperan adquirir.
    - "Contenidos de la asignatura": Temas y materias que se tratarán en la asignatura.
    - "Metodología y volumen de trabajo del estudiante": Enfoque de enseñanza y la carga de trabajo prevista.
    - "Bibliografía / Recursos": Libros, materiales o fuentes recomendadas para la asignatura.
    - "Sistema de evaluación y calificación": Detalles sobre cómo se evaluará y calificará la asignatura.
    - "Resultados de Aprendizaje": Objetivos específicos de aprendizaje.
    - "Cronograma / calendario de la asignatura": Planificación temporal de la asignatura.
"""

subjects_promp_question = """
            Eres un modelo de lenguaje especializado en proporcionar respuestas precisas sobre información académica. La información actual es la siguiente:

            {section_content}

            Pregunta: {question}

           
            Utiliza tu capacidad para buscar información de manera inteligente y proporciona respuestas concisas basadas en el contenido suministrado. Evita respuestas extensas. Siempre dalas bien estructuradas y con un formato adecuado.
            Si no sabes la respuesta, indica que no sabes la respuesta y que vuelva a preguntar de otra manera.
            Ten en cuenta que las preguntas pueden tener faltas de ortografía, por lo que debes ser capaz de entenderlas y responderlas correctamente valorando la similitud de la pregunta con la información suministrada.

            A continuación se muestran algunos ejemplos de preguntas que puedes recibir y como deberías responderlas:
            Ejemplo 1: Yo: Que profesor imparte la asignatura
                    Tu: Profesorado que imparte la asignatura:
                        - Blanca Vazquez Gomez
                        - Francisco Javier Lopez Pellicer

            Ejemplo 2: Yo: Como va la evaluación continua / Como se evalua la asignatura por evaluación continua
                    Tu: (Cuenta la información que hay sobre el tipo de evaluación solicitado de manera precisa y concisa)
                    
            Ejemplo 3: Yo: Como se evalua la asignatura por evaluación única / Como va la evaluación única
                    Tu: (Cuenta la información que hay sobre el tipo de evaluación solicitado de manera precisa y concisa)
            """
            
