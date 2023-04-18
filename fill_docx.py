import docx


# записываем в новый файл данные из словаря data
def write_docx(data):
    doc = docx.Document()
    for key in data.keys():
        doc.add_paragraph(f'{key} - {data[key]}')
    doc.save(f'{data["surname"]}.docx')


if __name__ == '__main__':
    write_docx(data)
