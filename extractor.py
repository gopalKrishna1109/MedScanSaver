import pdfplumber
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
    images = convert_from_bytes(
        pdf_file.read(),                     # convert PDF pages to images
        poppler_path=r"C:\Users\gopal\Release-25.12.0-0\poppler-25.12.0\Library\bin" 
    ) 
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img) + "\n"

    return text
