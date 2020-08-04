from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class EmailForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=40)])
    heard_about = StringField('Flavor Text!')
    job_position = StringField('Job Position')
    recipient_email = StringField('Recipient Email', validators=[Email()])
    submit = SubmitField('Generate Email')

class EmailFormSchema(FlaskForm):
    pass

class SendForm(FlaskForm):
    submit = SubmitField('Send Email')


