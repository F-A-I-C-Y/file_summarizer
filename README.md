# PDF & DOCX Summarizer Application

## Overview
This Streamlit-based application allows users to upload PDF or DOCX files and receive a summarized version of the document's text. It uses Google Generative AI to generate summaries from the extracted text of the uploaded file. Users can also copy the generated summary directly to the clipboard.

## Features
- **File Upload**: Supports both PDF and DOCX file uploads.
- **Text Extraction**: Extracts text from the uploaded PDF or DOCX files.
- **AI-Powered Summarization**: Uses Google Generative AI (via `google.generativeai`) to generate summaries of the extracted text.
- **Clipboard Copying**: Allows users to copy the generated summary to their clipboard with one click.

## Prerequisites

To run this application, you will need:
- **Python 3.7 or later**
- **Streamlit**: The web framework used for the UI.
- **Google Generative AI API Key**: Needed to access the summarization service.
- **PyPDF2**: For PDF text extraction.
- **python-docx**: For DOCX text extraction.
- **Pyperclip**: For clipboard functionality.
