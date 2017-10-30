from flask import Flask
from flask.ext.mail import Mail, Message

app = Flask(__name__)

# app.config.update(
#     DEBUG=True,
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT=465,
#     MAIL_USE_TLS=True,
# )

mail = Mail(app)

def sendmail():
    msg = Message(
        'Subject',
        sender='demoappsender@gmail.com',
        recipients=['krobinson@twilio.com'])
    msg.body = "Body here"
    mail.send(msg)

sendmail()
