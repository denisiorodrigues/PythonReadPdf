import PyPDF2
import os

main_folder = 'cnis' 
file_path = os.path.join(main_folder, 'file.pdf')

pdf_file = open(file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    xObject = page['/Resources']['/XObject'].get_object()
    for obj in xObject:
        print(xObject[obj])
        #if xObject[obj]['/Subtype'] == '/Image':
        #    size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
        #    data = xObject[obj]._data
        #    print(f"Found image: {obj}, size={size}, data={data[:20]}...")
pdf_file.close()

