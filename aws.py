import boto3
from botocore.exceptions import ClientError

class Aws:
    
    def get_caller_identity(self,access_key,secret_key) -> str:
        '''get caller indentity'''
        try:
            session = boto3.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
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