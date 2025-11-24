import os
import PyPDF2

def read_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        return "File not found."
    if filepath.endswith(".txt"):
        with open(filepath, "r") as f:
            return f.read()
    elif filepath.endswith(".pdf"):
        reader = PyPDF2.PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    else:
        return "Unsupported file type."
