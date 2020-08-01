from flask import Flask, render_template, url_for, flash, redirect, request 
import json
from forms import EmailForm, SendForm
# from config import Config
from email_send_v0 import send_email
import os


app = Flask(__name__, template_folder="../web_templates", static_folder="../static")
# app.config.from_object(Config)

app.config['SECRET_KEY'] = '4342821521556b6655d598110a54ca38'

information = {
        'recruiter_name': 'recruiter_name',
        'company': 'company_name',
        'job_position': 'job!!',
        'flavor_text': 'flavor town!',
    }

@app.route("/")
def hello():
    return render_template(r"template_web.html", information = information)


@app.route("/email_render", methods = ["GET","POST"])
def email_render():
    recipient_email = request.args.get('recipient_email')
    job_position = request.args.get('job_position')
    recruiter_name = request.args.get('recruiter_name')
    company_name = request.args.get('company_name')
    confirm_form = SendForm()
    if confirm_form.validate_on_submit():
        send_email(job_position, company_name, recruiter_name, recipient_email)
        ## Send email! 
    return render_template(r"template_email.html", recruiter_name = recruiter_name, job_position = job_position, company_name = company_name, recipient_email = recipient_email, form = confirm_form)


@app.route("/form", methods=['GET', 'POST'])
def form():
    info_form = EmailForm()
    if info_form.validate_on_submit():
        # flash(f"Email sent for {info_form.job_position.data} at {info_form.company_name.data} ", 'success')
        job_position = info_form.job_position.data
        company_name = info_form.company_name.data
        recruiter_name = info_form.recruiter_name.data
        recipient_email = info_form.recipient_email.data
        return redirect(url_for('email_render', job_position = job_position, company_name = company_name, recruiter_name = recruiter_name, recipient_email = recipient_email))
    # else:
    #     flash("failure!")
    #     return redirect(url_for('form'))
    return render_template(r"form.html", information = information, form = info_form)




if __name__ == '__main__':
    app.run(debug=True), 