import streamlit as st
from extractor import extract_text_pdfplumber, extract_text_ocr

st.title("MedScan Saver - PDF Extraction Test")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.write("PDF received!")

    # First try pdfplumber
    text = extract_text_pdfplumber(uploaded_file)

    if text.strip() != "":
        st.success("Extracted using pdfplumber (text-based PDF).")
        st.text(text)

    else:
        st.warning("No text found — attempting OCR (scanned PDF).")

        # Reset file pointer before OCR
        uploaded_file.seek(0)

        ocr_text = extract_text_ocr(uploaded_file)

        if ocr_text.strip() == "":
            st.error("OCR failed. The PDF might be corrupted.")
        else:
            st.success("Text extracted using OCR!")
            st.text(ocr_text)
