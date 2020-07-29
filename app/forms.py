from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class EmailForm(FlaskForm):
    company_name = StringField('company_name', validators=[DataRequired(), Length(min=2, max=40)])
    recruiter_name = StringField('recruiter_name', validators=[DataRequired(), Length(min=2, max=40)])
    job_position = StringField('job_position', validators=[DataRequired(), Length(min=2, max=40)])
    submit = SubmitField('Generate Email')


