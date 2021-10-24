# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import sys
import stdiomask
from database import Database
from utils import Utils
from aws import Aws

DB_CREDENTIALS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'aws.sqlite3')
MAX_ATTEMPS = 3

class colors:
    white = '\033[1;97m'
    red = '\033[0;91m'
    green = '\033[38;5;77m'
    yellow = '\033[38;5;227'
    purple = '\033[38;5;147m'
    blue = '\033[38;5;81m'
    end = '\033[0m'

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
        access_key = stdiomask.getpass(prompt='> Access Key: ', mask='*')
        secret_key =  stdiomask.getpass(prompt='> Secret Key ', mask='*')
        status_credentials = inst_aws.get_caller_identity(access_key.split(),secret_key.split()) #* test access and secret
        if status_credentials: 
            print('Success: Credentials have been registered\n')
            break
        if i == MAX_ATTEMPS-1: exit()
    passwd = stdiomask.getpass(prompt='> New Password ', mask='*')
    inst_db.create_credentials('access','secret','passwd')


if __name__ == '__main__':
    inst_db = Database(DB_CREDENTIALS)
    inst_os = Utils()
    inst_aws = Aws() 

    credentials = inst_db.check_if_exists()
    
    if not credentials:
        handle_new_credentials()
    
    credentials = handle_existing_credentials()
    
    print(credentials)
    # inst_db.close_connect()
