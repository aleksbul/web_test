import smtplib
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

from_email = testdata['from_email']
to_email = testdata['to_email']
pass_email = testdata['pass_email']
filename = 'log.txt'
subject = f"report {filename}"
message_body = 'Here is the text with test report'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

msg.attach(MIMEText(message_body, _subtype='plain'))

with open(filename, 'rb') as f:
    attach = MIMEBase('application', 'octet-stream')
    attach.set_payload(f.read())
    encoders.encode_base64(attach)
    attach.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(attach)

smtp_server = 'smtp.mail.ru'
smtp_port = 587

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(from_email, pass_email)

    server.sendmail(from_email, to_email, msg.as_string())

    print('The message was sent')
except Exception as e:
    print(f'Error {str(e)}')

finally:
    server.quit()
