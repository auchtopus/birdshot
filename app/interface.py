from flask import Flask, render_template, url_for, flash, redirect, request 
import json
from forms import EmailForm, SendForm, EmailFormSchema
# from config import Config
from email_send_v0 import send_email
from email_send_v0 import process_email.send_email_schema
import os


app = Flask(__name__, template_folder="../web_templates", static_folder="../static", )
# app.config.from_object(Config)

app.secret_key = os.environ.get('SECRET_KEY', 'dev')



@app.route("/email_render", methods = ["GET","POST"])
def email_render():
    recipient_email = request.args.get('recipient_email')
    job_position = request.args.get('job_position')
    heard_about = request.args.get('heard_about')
    company_name = request.args.get('company_name')
    confirm_form = SendForm()
    if confirm_form.validate_on_submit():
        send_email(job_position, company_name, recipient_email, heard_about)
        ## Send email! 
    return render_template(r"template_email.html", heard_about = heard_about, job_position = job_position, company_name = company_name, recipient_email = recipient_email, form = confirm_form)


@app.route("/form", methods=['GET', 'POST'])
def form():
    info_form = EmailForm()
    if info_form.validate_on_submit():
        job_position = info_form.job_position.data
        company_name = info_form.company_name.data
        heard_about = info_form.heard_about.data
        recipient_email = info_form.recipient_email.data
        send_email(job_position, company_name, recipient_email, heard_about)
        flash(f"Email sent for {info_form.job_position.data} at {info_form.company_name.data} ", 'success')
        return redirect(url_for('form', form=info_form))
        # return redirect(url_for('email_render', job_position = job_position, company_name = company_name, heard_about = heard_about, recipient_email = recipient_email))
    # else:
    #     flash("failure!")
    #     return redirect(url_for('form'))
    return render_template(r"form.html",  form = info_form)

@app.route("/form_test", methods=['GET', 'POST'])
def form_test():
    info_form = EmailFormSchema()
    if info_form.validate_on_submit():
        # flash(f"Email sent for {info_form.job_position.data} at {info_form.company_name.data} ", 'success')
        with open(f"../email_templates/recruitment.json", 'r') as schema:
            schema = json.load(schema)
            field_dict = schema["Fields"]
        for form_field in info_form:
            field_dict[form_field.name] = form_field.data
        send_email_schema(field_dict)
        return redirect(url_for('form_test', form=info_form))
        # return redirect(url_for('email_render', job_position = job_position, company_name = company_name, heard_about = heard_about, recipient_email = recipient_email))
    # else:
    #     flash("failure!")
    #     return redirect(url_for('form'))
    return render_template(r"form_loops.html",  form = info_form)



if __name__ == '__main__':
    app.run(debug=True), 