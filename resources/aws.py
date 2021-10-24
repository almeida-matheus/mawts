import boto3
from botocore.exceptions import ClientError

class Aws:

    def __init__(self,access_key,secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
    
    def get_caller_identity(self) -> str:
        try:
            session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
            )
            client = session.client('sts')
            return client.get_caller_idetity().get('Arn')
        except ClientError as e: 
            if e.response['Error']['Code'] == 'AccessDenied':
                pass
            else:
                pass
        except Exception as e:
            print(f'Error: Invalid Credentials')
        
    def get_profiles(self):
        session = boto3.Session().available_profiles