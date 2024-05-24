from PyPDF2 import PdfReader
import os

# Filtro para eliminar las líneas que no son parte del contenido de la asignatura
filters = [
    "Última modificación",
    "Aprobación",
    "Página"
]

# Función que recibe el nombre de un pdf y una lista de secciones y devuelve un diccionario con las secciones y su contenido
def GetSectionsFromPDF(pdf_name, sections, folder):
    # the pdf is in a folder called "pdf" in the root ../pdf
    pdf_reader = PdfReader(f"{folder}/{pdf_name}.pdf")
    text = ""
    sectionsExtracted = 1
    sections_with_text = {}
    lastSection = False
    section_delimiter = sections[sectionsExtracted]
    for page in pdf_reader.pages:
        for line in page.extract_text().split("\n"):
            if lastSection:
                text += line + "\n"
                continue
            if section_delimiter in line:
                currentSection = sections[sectionsExtracted - 1]
                sections_with_text[currentSection] = text
                text = ""
                sectionsExtracted += 1
                if sectionsExtracted == len(sections):
                    lastSection = True
                else:
                    section_delimiter = sections[sectionsExtracted]
            else:
                # si la linea no contiene ninguno de los filtros, añadirla al texto
                if not any(filter in line for filter in filters):   
                    text += line + "\n"
    
    sections_with_text[sections[sectionsExtracted - 1]] = text
    return sections_with_text

# Función que recibe una lista de asignaturas y una lista de secciones y devuelve un diccionario con las asignaturas y sus secciones
def buildSections(subjects, sections, folder):
    subjects_with_sections = {}
    for subject in subjects:
        subject_code = subjects[subject]
        pdf_name = subject_code + "-" + subject.replace(" ", "_")
        section_text = GetSectionsFromPDF(pdf_name, sections, folder)
        subjects_with_sections[subject] = section_text
    return subjects_with_sections

# Función que devuelve un diccionario con las asignaturas y sus códigos
def buildSubjects():
    subjects = {}

    for filename in os.listdir("pdf_sub"):
        subject = filename.split("-")
        subjects[subject[1].replace(".pdf", "").replace("_", " ")] = subject[0]
    return subjects
