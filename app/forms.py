from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class EmailForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=2, max=40)])
    recruiter_name = StringField('Recuiter Name', validators=[DataRequired(), Length(min=2, max=40)])
    job_position = StringField('Job Position', validators=[DataRequired(), Length(min=2, max=40)])
    recipient_email = StringField('Recipient Email', validators=[Email()])
    submit = SubmitField('Generate Email')


class SendForm(FlaskForm):
    submit = SubmitField('Send Email')


