#
# A simple and minimalistic command line based email client
# Main functions, argument parsing etc.
#
# Copyright (C)   2016    Madhav Datt
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#

from __future__ import print_function
from argparse import ArgumentParser
import sys
from authenticate import get_password, connect_email_account

# Email account authentication credentials
username = None
password = None

# Email action command parsers
mail_parser = ArgumentParser(description='Send a new email')
mail_parser.add_argument('-t', '--to', action='store', dest='to', required=False)
mail_parser.add_argument('-cc', '--cc', action='store', dest='cc', required=False)
mail_parser.add_argument('-bcc', '--bcc', action='store', dest='bcc', required=False)
mail_parser.add_argument('-s', '--subject', action='store', dest='subject', required=False)
mail_parser.add_argument('-h', '--html', action='append', dest='contents', required=False)
mail_parser.add_argument('-b', '--body', action='append', dest='contents', required=False)
mail_parser.add_argument('-a', '--attach', action='append', dest='contents', required=False)

# Parsers for reply and forward email commands
reply_parser = ArgumentParser(mail_parser, description='Reply to/forward an email')
reply_parser.add_argument('email_num', action='store', dest='email_num', type=int, choice=[1, 2, 3, 4, 5],
                          required=True, help='serial number of the email to forward/reply to')


def main():
    """
    Parse command line arguments passed and sign into email account
    """

    global username, password

    print("clmail Copyright (C) 2016 by Madhav Datt")
    print("Website: https://github.com/madhav-datt/clmail")
    print("See the GNU General Public Licence for license details.")
    print("\n")

    parser = ArgumentParser(description='clmail - minimalistic command line email')
    parser.add_argument('-u', '--username', action='store', dest='username', required=True,
                        help='username/email address (must be a gmail address)')
    parser.add_argument('-p', '--password', action='store', dest='password',
                        help='password for the email address', default=None)
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

    # Dictionary of email command functions
    cmd ={

    }

    while True:
        command_input = input('>>> ')
        command_input = command_input.split()
        cmd[command_input[0]](command_input[1:])

if __name__ == "__main__":
    main()
