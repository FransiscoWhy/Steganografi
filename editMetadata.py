import PyPDF2

def edit_pdf_metadata(input_pdf, output_pdf, new_metadata):
    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Copy pages and metadata from the input PDF to the output PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Update metadata
        pdf_writer.add_metadata(new_metadata)

        # Write the updated metadata to the output PDF file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

input_pdf = 'JAIIT_0502_0001+online.pdf'
output_pdf = 'output.pdf'
new_metadata = {'/Title': 'Sejarah Digital Forensik', '/Author': 'Tejo', '/Subject': 'Sistem Informasi' ,'/Keywords': 'Sistem informasi,desa,UMKM','/Created on': '12-2-2023','/Modified': '29-2-2024','/Creator': 'Syam' }

edit_pdf_metadata(input_pdf, output_pdf, new_metadata)

