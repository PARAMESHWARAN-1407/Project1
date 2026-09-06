from pypdf import PdfReader
from docx import Document
import os


def parse_document(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    text = ""

    # -------------------------
    # TXT / MD
    # -------------------------
    if ext in [".txt", ".md"]:

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    # -------------------------
    # PDF
    # -------------------------
    elif ext == ".pdf":

        reader = PdfReader(file_path)

        for page in reader.pages:
            text += page.extract_text() + "\n"

    # -------------------------
    # DOCX
    # -------------------------
    elif ext == ".docx":

        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        raise Exception("Unsupported file type")

    # -------------------------
    # PARSE FEATURES
    # -------------------------

    lines = text.split("\n")

    title = lines[0] if lines else "Untitled Project"

    features = []

    for line in lines[1:]:

        line = line.strip()

        if line:

            features.append({
                "name": line,
                "description": line
            })

    return {
        "title": title,
        "summary": text[:500],
        "features": features
    }