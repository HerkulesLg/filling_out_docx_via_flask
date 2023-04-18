from psw_generator import rand_psw
from fill_docx import write_docx
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = rand_psw()


# Главная страница
@app.route('/', methods=['POST', 'GET'])
def index():
    # Отправка формы на создание docx файла
    if request.method == 'POST':
        write_docx(request.form)
        if request.form["surname"]:
            return send_file(f'{request.form["surname"]}.docx', as_attachment=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)