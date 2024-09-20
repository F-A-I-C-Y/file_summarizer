import os
import streamlit as st
import google.generativeai as genai
import pyperclip
import docx
from PyPDF2 import PdfReader


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    doc_text = ""
    for paragraph in doc.paragraphs:
        doc_text += paragraph.text + "\n"
    return doc_text


def main():
  api_key = 'AIzaSyDCI_xeL7HhthSwbGNEkbas6fgAaRZhR2s'
  genai.configure(api_key=api_key)

  st.title("PDF & DOCX Summarizer")

  uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf","docx"])

  if uploaded_file is not None:
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()

    if file_extension == ".pdf":
      extracted_text = extract_text_from_pdf(uploaded_file)
    elif file_extension == ".docx":
      extracted_text = extract_text_from_docx(uploaded_file)
    else:
      st.warning("Unsupported file format!")

    if st.button("Generate Summary"):
      if extracted_text.strip():
        prompt = f"Summarize the following text: {extracted_text}"


        try:
          model = genai.GenerativeModel("gemini-1.5-flash")
          response = model.generate_content(prompt)
          summary = response.text
          
          st.session_state.generated_summary = summary
          st.session_state.copy_status = "Copy summary to Clipboard"

        except Exception as e:
          st.error(f"An error occurred: {e}")
          st.warning("We couldn't generate summary. Please try again later.")
      else:
        st.warning("The uploaded file is empty.")

    if "generated_summary" in st.session_state:
      st.subheader("Generated Summary:")
      summary_text_area = st.text_area("Generated Summary:",st.session_state.generated_summary, height=400,key="summary_content")
      if st.button("Copy summary to Clipboard"):
        pyperclip.copy(st.session_state.generated_summary)
        st.success("Summary copied to clipboard!")

if __name__ == "__main__":
  main()
