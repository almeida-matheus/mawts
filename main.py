# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import argparse
import sys
import stdiomask
import getpass
import resources

__version__ = '0.0.1'
__description__ = """\
Command line tool to manage aws credentials and automate tasks
"""
DB_CREDENTIALS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'aws.sqlite3')
MAX_ATTEMPS = 3
    
def handle_existing_credentials():
    for i in range(MAX_ATTEMPS):
        passwd = stdiomask.getpass(prompt='> Enter Password: ', mask='*')
        credentials = inst_db.get_credentials(passwd)
        if credentials:
            print('Success: Correct password\n')
            return credentials
        if i == MAX_ATTEMPS-1: exit()

def handle_new_credentials():
    for i in range(MAX_ATTEMPS):
        # access_key = stdiomask.getpass(prompt='> Access Key: ', mask='*')
        access_key = getpass.getpass(prompt='> Access Key: ', stream=None)
        secret_key = getpass.getpass(prompt='> Secret Key: ', stream=None)
        inst_aws = resources.Aws(access_key,secret_key) 
        status_credentials = inst_aws.get_caller_identity() #* test access and secret
        if status_credentials: 
            print('Success: Credentials have been registered\n')
            break
        if i == MAX_ATTEMPS-1: exit()
    passwd = getpass.getpass(prompt='> New Password: ', stream=None)
    inst_db.create_credentials('access','secret','passwd')


if __name__ == '__main__':
    color = resources.Color()
    inst_db = resources.Database(DB_CREDENTIALS)
    inst_os = resources.OSystem()

    parser = argparse.ArgumentParser(add_help=False ,description=__description__)
    parser.add_argument('--profile','-p', help='AWS profile to use')
    parser.add_argument('--version','-v', action='store_true', help='Show mawts version')
    parser.add_argument('--whoami','-w', action='store_true', help='Show AWS user info')
    parser.add_argument('--list','-l', action='store_true', help='List all available profiles')
    parser.add_argument('--help','-h', action='store_true', help='Show this help message')
    parser.add_argument('--export','-e', action='store_true', help='Export temporary credentials in default file')
    parser.add_argument('--rotate','-r', action='store_true', help='Rotate your credentials keys')
    args = parser.parse_args()

    arg_names = ['main', 'c1']
    d_args = dict(zip(arg_names, sys.argv))

    if d_args['c1'] == '--help' or d_args['c1'] == '-h':
        r = resources.Help().show()
        exit()

    if args.version:
        print(__version__)
        parser.exit()
    
    credentials = inst_db.check_if_exists()
    if not credentials:
        handle_new_credentials()
    credentials = handle_existing_credentials()
    
    inst_aws = resources.Aws(credentials[0],credentials[1])
    
    if args.list:
        inst_aws.get_profiles()
        parser.exit()
    
    # if d_args['c1']:
    #     inst_aws.assume_role()
    #     exit()

    # inst_db.close_connect()

