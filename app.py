from flask import Flask, render_template, request, flash, redirect
from contact_book import ContactBook
from dotenv import load_dotenv
import csv
import os

app = Flask(__name__)
app.secret_key = 'secret'
app.debug = True

load_dotenv()

@app.route(r'/', methods=['GET'])
def contact_book():
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

    return render_template('contact_book.html', contacts=contact_book._contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.form:
        contact_book = ContactBook()

        if request.form.get('password') == os.environ.get('PASSWORD_CONTACTS'):
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
            flash('Contact added successfully')

    return render_template('add_contact.html')

@app.route(r'/delete/<email>', methods=['POST'])
def delete_contact(email):
    
    if request.form:
        contact_book = ContactBook()
        try:
            if request.form.get('password') == os.environ.get('PASSWORD_CONTACTS'):
                with open('contacts.csv', 'r') as f:
                    reader = csv.reader(f)
                    for idx, row in enumerate(reader):
                        if idx == 0:
                            continue
                        contact_book.add(row[0], row[1], row[2])
                        contact_book.delete(email)
        except:
            pass

    return redirect('/')

if __name__ == "__main__":
    app.run()