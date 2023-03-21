from pypdf import PdfReader
import os
from helper import divisor, divisor_text
import json

head = []
body = []
footer = []

path = "files/extrat_text.txt"


def visitor_body(text, cm, tm, font_dict, font_size):
    y = tm[5]

    if text != "" and text != " ":
        f = open(path, "a", encoding="utf-8")
        f.write(str(tm) + '\n')
        f.write(text+'\n')
        f.close()

    if y > 457 and y < 474:
        head.append(text)

    if y > 24 and y < 35:
        footer.append(text)


# pdf reader object
reader = PdfReader('files/extrato.pdf')
if os.path.exists(path):
    os.remove(path)

path_print_terminal_text = "print_terminal_text.txt"

if os.path.exists(path_print_terminal_text):
    os.remove(path_print_terminal_text)

f = open(path_print_terminal_text, "a", encoding="utf-8")

separador_header = "-"*20 + " HEAD " + "-"*20
separador_body = "-"*20 + " BODY " + "-"*20
separador_footer = "-"*20 + " FOOTER " + "-"*20

qtd_pages = len(reader.pages)

for index in range(qtd_pages):
    head = []
    body = []
    footer = []

    page = reader.pages[index]
    page.extract_text(visitor_text=visitor_body)
    divisor(f"PAGINA {index+1}")
    print(separador_header)
    print("".join(head))
    print(separador_body)
    print("".join(body))
    print(separador_footer)
    print("".join(footer))
    print("-"*50 + "\n")

    f.write(f"\n\n{'-'*100}\nPAGINA {index+1}\n{'-'*100}\n")
    f.write(separador_header + "\n")
    f.write("".join(head) + "\n")
    f.write(separador_body + "\n")
    f.write("".join(body) + "\n")
    f.write(separador_footer+"\n")
    f.write("".join(footer)+"\n")

f.close()
