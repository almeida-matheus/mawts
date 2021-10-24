import os
from random import choice

class OSystem:

    def handle_dir(self,path='.aws'):
        ''' create a dir if not exit'''
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except:
            raise OSError("Error: Can't create directory here")

    def export_file(self,path_file,acccess_key,secret_key,session_token):
        template = f'''[default] 
        aws_session_token={session_token}
        aws_secret_access_key={secret_key}
        aws_access_key_id={acccess_key}
        ''' 
        try:
            file = open(path_file,'w')
            file.write()
        except:
            raise OSError("Error: Can't create file here")
        finally:
            file.close()

    def rm_file(self,path):
        if os.path.isfile(path):
            os.remove(path)

    def gen_passwd(self, qnt_chars):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%&<>'
        password = ''
        for c in range(qnt_chars):
            char = choice(chars)
            password += str(char)
        return password
