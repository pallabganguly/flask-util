from roadrunner import app
# from roadrunner.forms import ScriptForm
from roadrunner.validators import validate_filetype
from flask import render_template, redirect, request, flash
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	print("Logger: Index Page")
	# form = ScriptForm(request.form)
	# print(form.validate(), request.method)
	# if form.validate() and request.method == 'POST':
		# print("Logger:", form.scriptname.data, form.arguments.data)
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
	script = {'scriptname':'script.py', 'arguments':'args'}
	print("Debug: ", request)
	if 'image' not in request.files:
		flash('No file selected')
	else:
		file = request.files['image']
		print("Debug: ", file.filename)
		if file.filename == '' or file.filename == None:
			flash('No file selected')
		elif not validate_filetype(file.filename):
			flash('File type not allowed')
		else:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
			os.system('python3 scriptfolder/script.py')
			return render_template('success.html', script=script)
	
	# os.startfile("scriptfolder/count.xlsx")