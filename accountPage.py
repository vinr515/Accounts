#from flask import Flask
#from flask import render_template
import sqlite3

#(date text, pay text, card text, amount real, description text, category text)
"""
app = Flask(__name__)

@app.route('/')
def account_page():
    return render_template("full.html")
"""


conn = sqlite3.connect('accounts.db')
c = conn.cursor()
conn.commit()
conn.close()
