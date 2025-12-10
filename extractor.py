import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes

def extract_text_pdfplumber(pdf_file):
    """Extract text using pdfplumber only."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

def extract_text_ocr(pdf_file):
    """Extract text using OCR for scanned PDFs."""
    images = convert_from_bytes(pdf_file.read())  # convert PDF pages to images
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img) + "\n"

    return text
