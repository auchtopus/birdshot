import os
import smtplib
import sys
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText
from email.mime.image  import MIMEImage
from email.mime.application import MIMEApplication
from generate_email_v0 import generate_email


def send_email(position, company, recruiter_email, heard_about):
    print(sys.version)
    EMAIL_ADDRESS = os.environ.get('YALE_EMAIL')
    USERNAME =  "ajj38"
    EMAIL_PASSWORD = os.environ.get('YALE_PASSWORD')


    # configure message
    msg = MIMEMultipart()

    # generate body html
    # position = "Analyst"
    # company = "Good Morning"
    # recruiter = "Maria"
    # heard_about = "GOOD MORNING GOOD NIGHT"

    generate_email(position, company, recruiter_email, heard_about)

    msg['Subject'] = f"Fall 2020 internship opportunities at {company}"
    msg['From'] = "Anthony Jiang <anthony.jiang@yale.edu>"
    msg['To'] = recruiter_email ## import from flask app!


    with open(f"email_templates/{company}.html", 'rb') as mail_body:
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






if __name__ == "__main__":
    send_email("Hello", "goodbye", "goodmorning", "anthony75025@gmail.com")





## for sending emails to local
# with smtplib.SMTP('localhost', 1025) as smtp:
#     # encrypt traffic
#     # smtp.ehlo()
#     # smtp.starttls()
#     # smtp.ehlo()

#     # login
#     # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     print("sent SMTP request")
#     # 

#     subject = 'test email'
#     body = 'Hello world!'
#     msg = f'Subject: {subject}\n\n{body}'

#     # smtp.sendmail(EMAIL_ADDRESS, "anthony.jiang@yale.edu", msg)
