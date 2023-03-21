import camelot
import cv2
import os

file_path = os.path.join('files', 'extrato.pdf')
tables = camelot.read_pdf(file_path)
print(tables)
#<TableList n=1>
tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
print(tables[0])
#<Table shape=(7, 7)>
tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}

tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
tables[0].df # get a pandas DataFrame!