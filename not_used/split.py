import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('files/extrato.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Iterate through the pages and split each page into a new PDF file
for page_num in range(len(pdf_reader.pages)):
    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Add the current page to the writer object
    pdf_writer.add_page(pdf_reader.pages[page_num])

    # Write the new PDF file
    output_file = open(f'files/split/extrato_part_{page_num+1}.pdf', 'wb')
    pdf_writer.write(output_file)
    output_file.close()

# Close the input PDF file
pdf_file.close()
