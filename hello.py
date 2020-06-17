from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("simple.html")

"""Git Instructions
git init
git remote add origin https://github.com/vinr515/Accounts.git

git add hello.py
git commit -m "First commit!"
git push -u origin master"""
