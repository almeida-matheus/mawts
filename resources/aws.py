import boto3
from botocore.exceptions import ClientError

class Aws:

    def __init__(self,access_key,secret_key):
        if access_key: self.access_key = access_key
        if secret_key: self.secret_key = secret_key
    
    def get_caller_identity(self) -> str:
        try:
            session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
            )
            client = session.client('sts')
            return client.get_caller_identity().get('Arn')
        except ClientError as e:
            if e.response['Error']['Code'] == 'AccessDenied':
                print(f'Error: Access Denied')
            if e.response['Error']['Code'] == 'ExpiredToken':
                print(f'Error: Expired Temporary Credentials')
            if e.response['Error']['Code'] == 'InvalidClientTokenId':
                print(f'Error: Invalid Credentials')
            else:
                print(f'Error: Invalid Credentials')
        except Exception as e:
            print(f'Error: Invalid Credentials')

    def get_profiles(self):
        # session = boto3.Session().available_profiles

        try:
            session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
            )
            profiles = session.available_profiles
            for i, profile in enumerate(profiles):
                print(f'{i+1}: {profile}')
        except Exception as e:
            print(f'Error: Invalid Credentials')