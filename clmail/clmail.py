#
# A simple and minimalistic command line based email client
# Main functions, argument parsing etc.
#
# Copyright (C)   2016    Madhav Datt
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#

from __future__ import print_function
import argparse
import sys
from authenticate import get_password, connect_email_account

# Email account authentication credentials
username = None
password = None


def main():
    """
    Parse command line arguments passed and sign into email account
    """

    global username, password

    print("clmail Copyright (C) 2016 by Madhav Datt")
    print("Website: https://github.com/madhav-datt/clmail")
    print("See the GNU General Public Licence for license details.")
    print("\n")

    parser = argparse.ArgumentParser(description='clmail - minimalistic command line email')
    parser.add_argument('-u', '--username', action='store', dest='username',
                        help='username/email address (must be a gmail address)')
    parser.add_argument('-p', '--password', action='store', dest='password',
                        help='password for email address', default=None)
    parser.add_argument('-s', '--save-pass', action='store_true', dest='save',
                        help='save password securely in keyring', default=False)
    args = parser.parse_args(sys.argv)

    # Email authentication/login
    username = args.username
    if args.password is None:
        password = get_password(username)

    # To save password in keyring
    elif args.save:
        password = args.password
        connect_email_account(username, password)
    else:
        password = args.password


if __name__ == "__main__":
    main()
