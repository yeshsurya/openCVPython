import PyPDF2
import pytesseract
from PIL import Image

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate over each page and extract the text
        text = ""
        for page in pdf_reader.pages:
            # Convert the PDF page to an image
            image = page.to_image(resolution=300)

            # Perform OCR on the image using Tesseract
            ocr_text = pytesseract.image_to_string(image)

            # Append the extracted text to the result
            text += ocr_text

    return text

# Example usage
pdf_path = "path/to/your/pdf/file.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
