from pypdf import PdfReader
import os
from helper import divisor, divisor_text
import json
from employee import Employee

head = []
body = []
footer = []

employee_data = []

path = "files/extrat_text.txt"


def extract_employee(text, cm, tm, font_dict, font_size):
    x = tm[4]
    y = tm[5]

    if x == 55.0 and y == 473.72:
        print(text)
        employee_data.append(text)
        # employee.nit = text

    if x == 263.0 and y == 473.72:
        print(text)
        employee_data.append(text)
        # employee.cpf = text

    if x == 405.0 and y == 473.72:
        print(text)
        employee_data.append(text)
        # employee.name = text

    if x == 150.0 and y == 458.72:
        print(text)
        employee_data.append(text)
        # employee.birth_date = text

    if x == 455.0 and y == 458.72:
        print(text)
        employee_data.append(text)
        # employee.mothers_name = text


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

# Get Employee
page_one = reader.pages[0]
page_one.extract_text(visitor_text=extract_employee)

employee = Employee()

divisor("Employee JSON")
print("employee.nit")
employee.nit = employee_data[1]
print(employee.nit)
print(employee_data)
# print(json.dumps(employee))
print("-"*100)


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

#   PRINT
for index in range(qtd_pages):
    head = []
    body = []
    footer = []

    page = reader.pages[index]
    page.extract_text(visitor_text=visitor_body)
    # divisor(f"PAGINA {index+1}")
    # print(separador_header)
    # print("".join(head))
    # print(separador_body)
    # print("".join(body))
    # print(separador_footer)
    # print("".join(footer))
    # print("-"*50 + "\n")

    f.write(f"\n\n{'-'*100}\nPAGINA {index+1}\n{'-'*100}\n")
    f.write(separador_header + "\n")
    f.write("".join(head) + "\n")
    f.write(separador_body + "\n")
    f.write("".join(body) + "\n")
    f.write(separador_footer+"\n")
    f.write("".join(footer)+"\n")

f.close()
