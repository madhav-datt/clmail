#
# authenticate.py
#
# Store and use login credentials for clmail
#
# Copyright (C)   2016    Madhav Datt
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#

import getpass
import keyring
import keyring.errors


def connect_email_account(email, password):
    """
    Securely store password in Python keyring
    :param email: Email address for account to be used with clmail
    :param password: Password for email address
    :raises keyring.errors.PasswordSetError
    """
    # Raises keyring.errors.PasswordSetError if password not set
    keyring.set_password("clmail", email, password)
    keyring.set_password("yagmail", email, password)


def get_password(email):
    """
    :param email: Email address for account associated with clmail
    :return: Password for email address
    """

    # None if password doesn't exist
    password = keyring.get_password("clmail", email)

    if password is None:
        password = getpass.getpass("Password for {email_id}: ".format(email_id=email))
        connect_email_account(email, password)

    return password


def remove_email(email):
    """
    Remove stored email and password from keyring
    :param email: Email address for account associated with clmail
    """

    try:
        keyring.delete_password("clmail", email)
        keyring.delete_password("yagmail", email)
    except keyring.errors.PasswordDeleteError:
        pass
