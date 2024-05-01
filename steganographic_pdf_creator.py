from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import base64

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()
    return text

def encode_metadata(metadata):
    # Mengenkripsi metadata menggunakan base64_encode dan mengganti 'O' dengan 'S'
    encoded_metadata = base64.b64encode(metadata.encode()).decode()
    encoded_metadata = encoded_metadata.replace('O', 'S')
    return encoded_metadata

def create_steganographic_pdf(message, journal_pdf, logo_image, output_pdf):
    # Create a new PDF document
    c = canvas.Canvas(output_pdf, pagesize=(11.33 * 72, 14.67 * 72))  # Convert inches to points

    # Set text color to white (to be hidden)
    c.setFillColorRGB(1, 1, 1)

    # Encrypt message using base64 encoding
    encrypted_message = base64.b64encode(message.encode()).decode()

    # Add the encrypted message as hidden text
    c.drawString(100, 100, encrypted_message)

    # Set metadata directly using ReportLab
    c.setTitle(encode_metadata('Telkom University Surabaya'))
    c.setAuthor(encode_metadata('Telkom University Surabaya'))
    c.setSubject(encode_metadata('Coba'))
    c.setCreator(encode_metadata('Aldo'))  # Assuming "New Author" means creator

    # Add a new page for the main content
    c.showPage()

    # Set text color to black (for visible text)
    c.setFillColorRGB(0, 0, 0)

    # Add journal content
    journal_content = extract_text_from_pdf(journal_pdf)
    lines = journal_content.split('\n')
    y = 14.67 * 72 - 100  # Starting y-coordinate
    for line in lines:
        c.drawString(100, y, line)
        y -= 20  # Move to the next line

    # Add a new page for the end of the document (hidden)
    c.showPage()

    # Encrypt and hide metadata
    encoded_title = encode_metadata('New Author')
    encoded_author = encode_metadata('New Author')
    encoded_subject = encode_metadata('New Subject')
    encoded_creator = encode_metadata('New Creator')
    
    c.setTitle(encoded_title)
    c.setAuthor(encoded_author)
    c.setSubject(encoded_subject)
    c.setCreator(encoded_creator)

    # Save the PDF document
    c.save()

message = "Digital Forensik Ujicoba"
journal_pdf = "JAIIT_0502_0001+online.pdf"
logo_image = "logo.png"
output_pdf = "output/steganographic_pdf_with_journal_and_logo.pdf"

create_steganographic_pdf(message, journal_pdf, logo_image, output_pdf)
