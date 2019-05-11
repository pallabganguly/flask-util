from roadrunner import app
from roadrunner.forms import ScriptForm
from roadrunner.validators import validate_filetype
from flask import render_template, redirect, request, flash
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	print("Logger: Index Page")
	form = ScriptForm(request.form)
	# print(form.validate(), request.method)
	if form.validate() and request.method == 'POST':
		# print("Logger:", form.scriptname.data, form.arguments.data)
		print("Debug: ", request)
		if 'image' not in request.files:
			flash('No file selected')
		else:
			file = request.files['image']
			print(file)
			if file.filename == '':
				flash('No file selected')
			elif not validate_filetype(file.filename):
				flash('File type not allowed')
			else:
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
		os.system('python3 scriptfolder/'+form.scriptname.data)
		return render_template('success.html', form=form)
	return render_template('index.html', form=form)

@app.route('/upload', methods=['POST'])
def upload():
	print("Opening File")
	# os.startfile("scriptfolder/count.xlsx")