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
import mimetypes
import os
import smtplib
import time
import authenticate as auth
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logging import getLogger
from validate import validate_email


class SendMail:
    """
    Wrapper around the Python SMTP Library for sending emails
    """

    def __init__(self, username, host='smtp.gmail.com', port='587'):
        self.username = username
        self._login()
        self.host = host
        self.port = port

    def send(self, to, cc=None, bcc=None, subject=None, body=None, attachments=None):
        """"""

    def _build_message_content(self):
        """"""

    def _send_email(self, recipient_address, message_content):
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
            self.smtp.login(self.username, auth.get_password(self.username))


    def _get_mime_object(self, content_string):
        content_object = {
            'mime_object': None,
            'encoding': None,
            'main_type': None,
            'sub_type': None
        }

        if isinstance(content_string, dict):
            for x in content_string:
                content_string, content_name = x, content_string[x]
        else:
            content_name = os.path.basename(content_string)

        # pylint: disable=unidiomatic-typecheck
        is_raw = type(content_string) == raw
        if os.path.isfile(content_string) and not is_raw:
            with open(content_string, 'rb') as f:
                content_object['encoding'] = 'base64'
                content = f.read()
        else:
            content_object['main_type'] = 'text'

            if is_raw:
                content_object['mime_object'] = MIMEText(content_string, _charset=self.encoding)
            else:
                content_object['mime_object'] = MIMEText(
                    content_string, 'html', _charset=self.encoding)
                content_object['sub_type'] = 'html'

            if content_object['sub_type'] is None:
                content_object['sub_type'] = 'plain'
            return content_object

        if content_object['main_type'] is None:
            content_type, _ = mimetypes.guess_type(content_string)

            if content_type is not None:
                content_object['main_type'], content_object['sub_type'] = content_type.split('/')

        if (content_object['main_type'] is None or
                    content_object['encoding'] is not None):
            if content_object['encoding'] != 'base64':
                content_object['main_type'] = 'application'
                content_object['sub_type'] = 'octet-stream'

        mime_object = MIMEBase(content_object['main_type'], content_object['sub_type'],
                               name=content_name)
        mime_object.set_payload(content)
        content_object['mime_object'] = mime_object
        return content_object
