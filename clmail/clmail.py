#
# A simple and minimalistic command line based email client
# Main functions, argument parsing etc.
#
# Copyright (C)   2016    Madhav Datt
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
#

from __future__ import print_function
import argparse

#
username = None
password = None


def main():
    """
    Parse command line arguments passed and sign into email account
    """

    print("clmail Copyright (C) 2016 by Madhav Datt")
    print("Website: https://github.com/madhav-datt/clmail")
    print("See the GNU General Public Licence for license details.")
    print("\n")

    parser = argparse.ArgumentParser(description='clmail - minimalistic command line email')
    parser.add_argument('-u', '--username', help='username/email address (must be a gmail address)')
    parser.add_argument('-p', '--password', help='password for email address', default=None)
    args = parser.parse_args()


if __name__ == "__main__":
    main()
