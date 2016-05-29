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
import authenticate as auth
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from log import loggers


class SendMail:
    """
    Wrapper around the Python SMTP Library for sending emails
    """

    def __init__(self, username, host='smtp.gmail.com', port='587'):
        self.username = username
        self._login()

    def send(self, to, cc=None, bcc=None, subject=None, body=None, attachments=None):
        """"""

    def _login(self):
        """
        Login to the SMTP server using password. `login` only needs to be manually run when the
        connection to the SMTP server was closed by the user.
        """
        self.smtp = smtplib.SMTP(self.host, self.port, **self.kwargs)
        self.smtp.set_debuglevel(self.debuglevel)
        if self.starttls:
            self.smtp.ehlo()
            if self.starttls is True:
                self.smtp.starttls()
            else:
                self.smtp.starttls(**self.starttls)
            self.smtp.ehlo()
        self.is_closed = False
        if not self.smtp_skip_login:
            password = self._handle_password(password)
            self.smtp.login(self.user, password)
