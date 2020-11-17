from flask_mail import Message
from flask import render_template
from ..bootstrap import mail
from ..constants import MAIL_USERNAME, WEB_URL
import os

def __send_email(subject, recipient, template, data):
    try:
        msg = Message(subject=subject,sender=MAIL_USERNAME, recipients=[recipient])
        msg.html = render_template(template, data=data)
        mail.send(msg)
    except Exception as error:
        raise Exception(error.args[0])
    
def verification_session_email(subject, recipient, data):
    data['WEB_URL'] = WEB_URL
    __send_email(subject, recipient, "mail/validate_session.html", data)