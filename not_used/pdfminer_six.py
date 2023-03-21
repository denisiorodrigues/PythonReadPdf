import os
# from pdfminer.high_level import extract_text

main_folder = 'files' 
file_path = os.path.join(main_folder, 'extrato.pdf')

# text = extract_text(file_path)
# print(text)

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
output = StringIO()
with open(file_path, 'rb') as pdf_file:
    extract_text_to_fp(pdf_file, output, laparams=LAParams(), output_type='text', codec=None)
with open('example.txt', 'a') as html_file:
    html_file.write(output.getvalue())