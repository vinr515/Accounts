from flask import Flask
from flask import render_template
from flask import request
import sqlite3

#(year integer, month integer, date integer, pay text, card text, amount real,
#description text, category text)

app = Flask(__name__)

@app.route('/')
def account_page():
    return render_template("full.html")

@app.route('/newpage', methods=['POST'])
def new_page():
    formNames = ['purchaseDate', 'type', 'cardName', 'amount', 'description', 'category']
    info = ['']*len(formNames)
    for i in range(len(formNames)):
        info[i] = request.form[formNames[i]]
    date, payType, cardName, amount = info[0], info[1], info[2], info[3]
    description, category = info[4], info[5]
    
    year, month, day = map(int, date.split('-'))
    amount = round(float(amount), 2)
    print(year, month, day, payType, cardName, amount, description)
    print(category)
    return render_template("simple.html")

"""
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
conn.commit()
conn.close()
"""
