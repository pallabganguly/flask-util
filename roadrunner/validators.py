from roadrunner import app

ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']

def validate_filetype(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS