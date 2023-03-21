import PyPDF2

pdf_file = open('files/extrato.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

num_pages = len(pdf_reader.pages)

print(num_pages)

for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    resources = page['/Resources']
    if '/Font' in resources:
        fonts = resources['/Font']
        for font in fonts:
            font_name = fonts[font]['/BaseFont']
            print('Page {} - Font: {}'.format(page_num+1, font_name))

