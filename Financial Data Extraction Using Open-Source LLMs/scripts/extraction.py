import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using pdfplumber.
    """
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_path = 'data/raw_pdfs/sample_report.pdf'
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
