import using_pypdfium2 as pdfium
import os

file_path = os.path.join('files', 'extrato.pdf')
pdf = pdfium.PdfDocument(file_path)
version = pdf.get_version()  # get the PDF standard version
n_pages = len(pdf)  # get the number of pages in the document

for item in pdf.get_toc():
  
    if item.n_kids == 0:
        state = "*"
    elif item.is_closed:
        state = "-"
    else:
        state = "+"
    
    if item.page_index is None:
        target = "?"
    else:
        target = item.page_index + 1
    
    print(
        "    " * item.level +
        "[%s] %s -> %s  # %s %s" % (
            state, item.title, target, item.view_mode,
            [round(c, n_digits) for c in item.view_pos],
        )
    )