import PyPDF2
import tabula
import os
from helper import divisor 

file_path = os.path.join('files', 'extrato.pdf')

print(file_path)

# Open the PDF file in read-binary mode
# with open(file_path, 'rb') as file:
#    Create a PyPDF2 object to read the PDF file
    # pdf_reader = PyPDF2.PdfReader(file)
# 
    #Get the first page of the PDF file
    # page = pdf_reader.pages[0]
# 
    #Extract the table from the page using tabula-py
    # table = tabula.read_pdf(file, pages=2, stream=True)[0]
# 
    #Print the table
    # print(table)


table = tabula.read_pdf(file_path, pages="all", encoding="latin 1")

# Print the table
print(len(table))
divisor("conteúdo")
print(table)