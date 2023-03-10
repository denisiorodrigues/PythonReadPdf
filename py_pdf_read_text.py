import PyPDF2
import os

#Obter o caminho completo
print(os.getcwd())

def divisor (title=''):
    total = 50
    print("-"*total)
    print(title.upper().center(total))
    print("-"*total)


# pdf file object
# you can find find the pdf file with complete code in below
main_folder = 'cnis' 
file_path = os.path.join(main_folder, 'file.pdf')
pdfFileObj = open(file_path, 'rb')
# pdf reader object
reader = PyPDF2.PdfReader(pdfFileObj)
# number of pages in pdf

divisor("Properties File")
print("Size: ", os.path.getsize(file_path), "bytes")
print(reader.get_fields())
print(reader.metadata)

divisor('get_fields')
print(reader.get_fields())

divisor('get_form_text_fields')
print(reader.get_form_text_fields())

divisor('is_encrypted')
print(reader.is_encrypted)

page_number = 0
divisor(f'page {page_number}')
print(reader.pages[page_number])

divisor('Total pages')
print(len(reader.pages))

# a page object
#divisor('Extracting text from page')
#page_number = 0
page = reader.pages[page_number]
## extracting text from page.
## this will print the text you can also save that into String
print(page.extract_text())
#
#divisor('Page')
#
#print(type(page))
#print(page)
#
#divisor('Visitor body')
#
#parts = []
#
#
#def visitor_body(text, cm, tm, font_dict, font_size):
#    y = tm[5]
#    if y > 50 and y < 720:
#        parts.append(text)
#
#
#page.extract_text(visitor_text=visitor_body)
#text_body = "".join(parts)
#
#print(type(text_body))
#print(text_body)
#divisor('Decode')
#print(text_body.encode('utf8').decode('utf8'))
#
#
##IMAGES
count = 0
page = reader.pages[0]
for image_file_object in page.images:
    with open(f"{main_folder}/{str(count) + image_file_object.name}", "wb") as fp:
        fp.write(image_file_object.data)
        count += 1