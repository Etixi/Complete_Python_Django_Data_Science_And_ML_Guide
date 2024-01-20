from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

html_template = Template(Path('../Section61_Sending_Emails/templates/template.html').read_text())
print(html_template)
html_content = html_template.substitute({'name': 'Bogdan', 'date': 'tomorrow'})
# print(html_template.is_valid())

my_email = EmailMessage()


my_email['from'] = 'Bogdan'
my_email['to'] = 'test@test.com'
my_email['subject'] = "Hello from Python"
my_email.set_content(html_content, 'html')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print('Email was sent')