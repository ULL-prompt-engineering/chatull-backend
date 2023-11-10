from PyPDF2 import PdfReader

def GetSectionsFromPDF(pdf_name, sections):
    pdf_reader = PdfReader(f"{pdf_name}.pdf")
    text = ""
    sectionsExtracted = 1
    sections_with_text = {}
    section_delimiter = sections[sectionsExtracted]
    for page in pdf_reader.pages:
        for line in page.extract_text().split("\n"):
            if section_delimiter in line:
                currentSection = sections[sectionsExtracted - 1]
                sections_with_text[currentSection] = text
                text = ""
                sectionsExtracted += 1
                if sectionsExtracted == len(sections):
                    break
                else:
                    section_delimiter = sections[sectionsExtracted]
            else:
                text += line + "\n"
    return sections_with_text

def buildSubjectsSections(subjects, sections):
    subjects_with_sections = {}
    for subject in subjects.values():
        sections = GetSectionsFromPDF(subject, sections)
        subjects_with_sections[subject] = sections
    return subjects_with_sections



def main():
    #subjects = {
    #    "Procesadores del Lenguaje": "PL",
    #    "Interfaces Inteligentes": "II",
    #    "Robótica Computacional": "RC",
    #}
    subjects = {
        "Procesadores del Lenguaje": "PL",
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

    all_information = buildSubjectsSections(subjects, sections)
    print(all_information["PL"]["Datos descriptivos de la asignatura"])

if __name__ == "__main__":
    main()
