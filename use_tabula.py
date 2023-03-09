import PyPDF2
import tabula
import os

main_folder = 'cnis' 
file_path = os.path.join(main_folder, 'file.pdf')

# Open the PDF file in read-binary mode
with open(file_path, 'rb') as file:
    # Create a PyPDF2 object to read the PDF file
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the first page of the PDF file
    page = pdf_reader.pages[0]

    # Extract the table from the page using tabula-py
    table = tabula.read_pdf(file, pages=1, stream=True)[0]

    # Print the table
    print(table)
