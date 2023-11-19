from PyPDF2 import PdfReader

filters = [
    "Última modificación",
    "Aprobación",
    "Página"
]

def GetSectionsFromPDF(pdf_name, sections):
    pdf_reader = PdfReader(f"{pdf_name}.pdf")
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

def buildSubjectsSections(subjects, sections):
    subjects_with_sections = {}
    for subject in subjects.values():
        section_text = GetSectionsFromPDF(subject, sections)
        subjects_with_sections[subject] = section_text
    return subjects_with_sections