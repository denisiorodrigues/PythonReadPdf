from pypdf import PdfReader
import os

#file_name = os.path.abspath("exemple.pdf")
#print("Arquivo: ", file_name)
#print(parthComplete, type(parthComplete))

file_name = "D:\workspace\python\PythonReadPdf\exemple.pdf"
#reader = PdfReader(file_name)
#number_of_pages = len(reader.pages)
#page = reader.pages[0]
#text = page.extract_text()
#print(text)


#dirlist = os.listdir("file/.") 
#for i in dirlist:
#    filename = os.path.abspath(i)
#    print(filename)
#    reader = PdfReader(filename)
#    number_of_pages = len(reader.pages)
#    page = reader.pages[0]
#    text = page.extract_text()
#    print(text)


reader = PdfReader(file_name)

for page in reader.pages:
    print(page)
    #if "/Annots" in page:
    #    for annot in page["/Annots"]:
    #        subtype = annot.get_object()["/Subtype"]
    #        if subtype == "/Text":
    #            print(annot.get_object()["/Contents"])
    #else :
    #    print(f"nada foi encontrado na página {page}")
#