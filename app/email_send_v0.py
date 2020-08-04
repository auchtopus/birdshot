import os, sys
import json
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText
from email.mime.image  import MIMEImage
from email.mime.application import MIMEApplication
from generate_email_v0 import generate_email


class process_email():
    num_emails = 0

    @classmethod
    def generate_email_schema(cls, field_dict, schema):
        cls.num_emails +=1

        with open(f"../email_templates/{schema}.json", "r") as schema_file:
            schema = json.load(schema_file)



        ## append to a manifest
        with open(f"../email_buffer/manifest.json", "w") as manifest_file:
            ## add the field_dict to the schema, add a field for the number, save
            pass

        ## save email to the buffer
        with open(f"../email_buffer/{cls.num_emails}.html", "w") as output_file: ## configure relative path?
            print(head, file=output_file)
            print(body, file=output_file)


    def send_email_schema(field_dict, schema_name):

        # Account information
        EMAIL_ADDRESS = os.environ.get('MAIL')
        USERNAME =  "ajj38"
        EMAIL_PASSWORD = os.environ.get('YALE_PASSWORD')


        # load schema
        with open(f"../email_templates/{schema_name}.json", 'r') as schema_load:
            schema = json.load(schema_load)

        # Load fieds

        
        # configure message


        

        generate_email(position, company, recruiter_email, heard_about)


        msg = MIMEMultipart()

        msg['Subject'] = f"Fall 2020 internship opportunities at {company}"
        msg['From'] = "Anthony Jiang <anthony.jiang@yale.edu>"
        msg['To'] = recruiter_email ## import from flask app!

        with open(f"email_buffer/{company}.html", 'rb') as mail_body:
            msg_text = MIMEText(mail_body.read(),'html', 'utf-8')
        msg.attach(msg_text)

        with open('/Users/antonsquared/Google_Drive/Jobs/Anthony_Jiang_Resume_SWE.pdf', 'rb') as attachment:
            attach = MIMEApplication(attachment.read(),_subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment', filename="Anthony Jiang Resume")
        msg.attach(attach)  

        with open(f"web_templates/signature.html", 'rb') as mail_signature:
            signature = MIMEText(mail_signature.read(),'html','utf-8')
        msg.attach(signature)
        with smtplib.SMTP('mail.yale.edu', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            # login
            smtp.login(USERNAME, EMAIL_PASSWORD)

            smtp.send_message(msg)


    
def send_email(position, company, recruiter_email, heard_about):
    print(sys.version)
    EMAIL_ADDRESS = os.environ.get('YALE_EMAIL')
    USERNAME =  "ajj38"
    EMAIL_PASSWORD = os.environ.get('YALE_PASSWORD')


    # configure message
    msg = MIMEMultipart()

    generate_email(position, company, recruiter_email, heard_about)

    msg['Subject'] = f"Fall 2020 internship opportunities at {company}"
    msg['From'] = "Anthony Jiang <anthony.jiang@yale.edu>"
    msg['To'] = recruiter_email ## import from flask app!

    with open(f"email_buffer/{company}.html", 'rb') as mail_body:
        msg_text = MIMEText(mail_body.read(),'html', 'utf-8')
    msg.attach(msg_text)

    with open('/Users/antonsquared/Google_Drive/Jobs/Anthony_Jiang_Resume_SWE.pdf', 'rb') as attachment:
        attach = MIMEApplication(attachment.read(),_subtype="pdf")
    attach.add_header('Content-Disposition', 'attachment', filename="Anthony Jiang Resume")
    msg.attach(attach)  

    with open(f"web_templates/signature.html", 'rb') as mail_signature:
        signature = MIMEText(mail_signature.read(),'html','utf-8')
    msg.attach(signature)
    with smtplib.SMTP('mail.yale.edu', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        # login
        smtp.login(USERNAME, EMAIL_PASSWORD)

        smtp.send_message(msg)






# if __name__ == "__main__":
#     send_email("Hello", "goodbye", "goodmorning", "anthony75025@gmail.com")





