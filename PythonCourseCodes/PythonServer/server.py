from flask import Flask, redirect, render_template, url_for, request
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def work(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./PythonServer/database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('./PythonServer/database.csv', newline='',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database2, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        print("Something Went Wrong")
