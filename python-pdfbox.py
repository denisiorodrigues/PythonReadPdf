import pdfbox
import os

p = pdfbox.PDFBox()
main_folder = 'cnis' 
file_path = os.path.join(main_folder, 'file.pdf')

print(p.extract_text(file_path))   # writes text to /path/to/my_file.txt
p.pdf_to_images(file_path)  # writes images to /path/to/my_file1.jpg, /path/to/my_file2.jpg, etc.
p.extract_images(file_path) # writes images to /path/to/my_file-1.png, /path/to/my_file-2.png, etc.


pdf_ref = pdfbox.PDFBox()
print(pdf_ref.extract_text(main_folder))