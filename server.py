# No noobServer todos os inputs foram colados "à mão". Podemos usar a
# funv render_template do pacote Flask para importar arquivos 'html', 'css'
# e 'js' previamente criados

# DETALHE: precisamos criar uma pasta 'templates' para o render_template
# ler os .html.
# Arquivos .css precisam ser salvos no folder 'static/style.css'. O path
# no 'index.html' precisa indicar esse novo caminho.

# $ export FLASK_APP=server.py
# to run it use $ flask run
# $ export FLASK_ENV=development and run the app again $ flask run.

from flask import Flask, url_for, render_template, request, redirect
import csv

app = Flask(__name__)  # sets app name as __main__
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# write to txt file
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         comment = data["comment"]
#         file = database.write(f'\n{email}, {subject},{comment}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        comment = data["comment"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, comment])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # grab data and saves is as dict
            write_to_csv(data)
            return redirect(url_for('my_home'))
        except:
            return 'did not save to database'
    else:
        return "ooops! something went wrong"
