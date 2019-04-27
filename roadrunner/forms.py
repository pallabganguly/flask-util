from wtforms import Form, StringField, SubmitField, validators

class ScriptForm(Form):
    scriptname = StringField('Enter Name', [validators.DataRequired()])
    arguments = StringField('Enter any arguments')