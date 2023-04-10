import smtplib
import config
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version

def send_password_reset_mail(email, token):
    user = 'obrozovatelnaap.claudiuss@gmail.com'
    password = 'otnvrnhvrovyxfkm'

    recipients = email
    sender = 'obrozovatelnaap.claudiuss@gmail.com'
    subject = 'Восстановление пароля'
    text = f'Перейдите по ссылке для восстановления пароля:{config.site_url}/forgot_password/{token}'
    html = '<html><head></head><body><h7>' + text + '</h7></body></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()


def send_mail(email,coup):
    user = 'obrozovatelnaap.claudiuss@gmail.com'
    password = 'otnvrnhvrovyxfkm'

    recipients = email
    sender = 'obrozovatelnaap.claudiuss@gmail.com'
    subject = 'Купон'
    text = 'Купон: '+coup
    html = '<html><head></head><body><h7>' + text + '</h7></body></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
