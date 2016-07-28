#
# SendMail Class - a wrapper around the SMTP Python Package
# Send emails from @gmail.com addresses
#
# Copyright (C)   2016    Madhav Datt
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#

import yagmail


def send():
    """
    Wrapper around the send function of the yagmail API
    """
    yagmail.SMTP(username).send(to, cc, bcc, contents)
