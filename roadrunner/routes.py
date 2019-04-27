from roadrunner import app
from roadrunner.forms import ScriptForm
from flask import render_template, redirect, request
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print("Logger: Index Page")
    form = ScriptForm(request.form)
    print(form.validate(), request.method)
    os.system('python3 scriptfolder/script.py')
    if form.validate() and request.method == 'POST':
        print("Logger:", form.scriptname.data, form.arguments.data)
        os.system('python3 scriptfolder/'+form.scriptname.data)
        return render_template('success.html', form=form)
    return render_template('index.html', form=form)

@app.route('/open')
def open():
    print("Opening File")
    # os.startfile("scriptfolder/count.xlsx")