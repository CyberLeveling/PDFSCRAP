import requests
import pdfplumber
import io

def extract_text_from_pdf_url(pdf_url):
    # Fetch the PDF content from the URL
    response = requests.get(pdf_url)
    with pdfplumber.open(io.BytesIO(response.content)) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Example usage:
pdf_url = 'https://example.com/example.pdf'
extracted_text = extract_text_from_pdf_url(pdf_url)
print(extracted_text)
