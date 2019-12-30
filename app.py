from flask import Flask, render_template, request
from contact_book import ContactBook
from dotenv import load_dotenv
import csv
import os

app = Flask(__name__)

load_dotenv()

@app.route(r'/', methods=['GET'])
def contact_book():
    print(os.getenv('TEST_ENV'))
    return render_template('contact_book.html')

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.form:
        contact_book = ContactBook()

        try:
            with open('contacts.csv', 'r') as f:
                reader = csv.reader(f)
                for idx, row in enumerate(reader):
                    if idx == 0:
                        continue
                    contact_book.add(row[0], row[1], row[2])
        except:
            pass
        
        contact_book.add(request.form.get('name'), request.form.get('phone'), request.form.get('email'))

    return render_template('add_contact.html')

if __name__ == "__main__":
    app.run()