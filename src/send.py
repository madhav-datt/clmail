#
# send.py
#
# SendMail Class - a wrapper around the SMTP Python Package
# Send emails from @gmail.com addresses
#
# Copyright (C)   2016    Madhav Datt
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


class SendMail:
    """
    Wrapper around the Python SMTP Library for sending emails
    """

    def __init__(self):
        pass


    def send(self, username, password, to_email, cc_email, bcc_email, ):

# fromaddr = "YOUR EMAIL"
# toaddr = "EMAIL ADDRESS YOU SEND TO"
#
# msg = MIMEMultipart()
#
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "SUBJECT OF THE EMAIL"
#
# body = "TEXT YOU WANT TO SEND"
#
# msg.attach(MIMEText(body, 'plain'))
#
# filename = "NAME OF THE FILE WITH ITS EXTENSION"
# attachment = open("PATH OF THE FILE", "rb")
#
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#
# msg.attach(part)
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(fromaddr, "YOUR PASSWORD")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()