from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("files/extrato.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)

with open("files/compress/out.pdf", "wb") as f:
    writer.write(f)