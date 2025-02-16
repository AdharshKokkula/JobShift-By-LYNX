import fitz

def extract_text_from_pdf(file_data):
  pdf_doc = fitz.open(stream=file_data, filetype='pdf')
  text = " ".join([page.get_text("text") for page in pdf_doc])
  return text

