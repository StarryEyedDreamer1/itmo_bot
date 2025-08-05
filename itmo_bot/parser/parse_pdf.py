
import pdfplumber
import pandas as pd

def extract_disciplines(pdf_path):
    data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            for line in text.split('\n'):
                if any(x in line.lower() for x in ['дисциплина', 'практика']):
                    parts = line.split()
                    if len(parts) >= 2:
                        name = ' '.join(parts[:-1])
                        data.append({'discipline': name})
    return pd.DataFrame(data)
