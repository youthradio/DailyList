from flask import Flask, render_template, request
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "scripts@youthradio.org"
gmail_pwd = "TrBDXGZ9"

def mail(to, subject, text):
    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'html'))

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()


app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')


@app.route("/submit", methods=['POST'])
def submission():
    mail("applab@youthradio.org", "Daily List Test", render_template('dailylist2.html', form=request.form))
    return render_template('dailylist2.html', form=request.form)



if __name__ == "__main__":
    app.run(debug=True)
