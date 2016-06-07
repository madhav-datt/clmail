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
        self.debug_point = 0

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
        self.smtp = smtplib.SMTP(self.host, self.port)
        self.smtp.set_debuglevel(self.debug_point)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.is_closed = False
        self.smtp.login(self.username, auth.get_password(self.username))

    def _get_mime_object(self, email_content):
        """
        Build MIME Objects from email content strings
        :param email_content:
        :return: mime_content_object
        """
        mime_content_object = {'mime_object': None, 'encoding': None, 'main_type': None, 'sub_type': None}

        if isinstance(email_content, dict):
            for x in email_content:
                email_content, content_name = x, email_content[x]
        else:
            content_name = os.path.basename(email_content)

        # pylint: disable=unidiomatic-typecheck
        is_raw = type(email_content) == raw
        if os.path.isfile(email_content) and not is_raw:
            with open(email_content, 'rb') as f:
                mime_content_object['encoding'] = 'base64'
                content = f.read()
        else:
            mime_content_object['main_type'] = 'text'

            if is_raw:
                mime_content_object['mime_object'] = MIMEText(email_content, _charset=self.encoding)
            else:
                mime_content_object['mime_object'] = MIMEText(
                    email_content, 'html', _charset=self.encoding)
                mime_content_object['sub_type'] = 'html'

            if mime_content_object['sub_type'] is None:
                mime_content_object['sub_type'] = 'plain'
            return mime_content_object

        if mime_content_object['main_type'] is None:
            content_type, _ = mimetypes.guess_type(email_content)

            if content_type is not None:
                mime_content_object['main_type'], mime_content_object['sub_type'] = content_type.split('/')

        if mime_content_object['main_type'] is None or mime_content_object['encoding'] is not None:
            if mime_content_object['encoding'] != 'base64':
                mime_content_object['main_type'] = 'application'
                mime_content_object['sub_type'] = 'octet-stream'

        mime_object = MIMEBase(mime_content_object['main_type'], mime_content_object['sub_type'], name=content_name)
        mime_object.set_payload(content)
        mime_content_object['mime_object'] = mime_object
        return mime_content_object
