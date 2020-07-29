from flask import Flask, render_template, url_for, flash, redirect, request 
import json
from forms import EmailForm
# from config import Config
import os


app = Flask(__name__, template_folder="../web_templates", static_folder="../static")
# app.config.from_object(Config)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

information = {
        'recruiter': 'recruiter_name',
        'company': 'company_name',
        'job_title': 'job!!',
        'flavor_text': 'flavor town!',
    }

@app.route("/")
def hello():
    return render_template(r"template_web.html", information = information)


@app.route("/email_render")
def email_render():
    return render_template(r"template_email.html", information = information)


@app.route("/form", methods=['GET', 'POST'])
def form():
    info_form = EmailForm()
    if info_form.validate_on_submit():
        flash(f"Email sent for {info_form.job_position.data} at {info_form.company_name.data} ", 'success')
        return redirect(url_for('email_render'))
    return render_template(r"form.html", information = information, form = info_form)




if __name__ == '__main__':
    app.run(debug=True)