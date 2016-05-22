#
# send.py
#
# SendMail Class - a wrapper around the SMTP Python Package
# Send emails from @gmail.com addresses
#
# Copyright (C)   2016    Madhav Datt
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#

import email.encoders
import logging
import mimetypes
import os
import smtplib
import time
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import authenticate


class SendMail:
    """
    Wrapper around the Python SMTP Library for sending emails
    """

    def __init__(self):
        pass


    def send(self, username, password, to, cc, bcc, ):

