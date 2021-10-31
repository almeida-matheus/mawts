import sqlite3
import bcrypt

class Database:

    def __init__(self,db_credentials) -> str:
        '''constructor to create cursor to connect to db and create a table with credentials if not exist'''
        try:
            self.con = sqlite3.connect(db_credentials)
            self.cursor = self.con.cursor()

            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id integer PRIMARY KEY AUTOINCREMENT,
                access_key text,
                secret_key text,
                passwd text
            );
            ''')
        except Exception as e:
            print(f'Error {e}')

    def check_if_exists(self):
        '''scan database check if exist the values'''
        self.cursor.execute('SELECT * FROM user WHERE id=1')
        result = self.cursor.fetchall()
        if result: return True
    
    def get_credentials(self,passwd=None):
        '''scan database to get credentials if hash is checked'''
        try:
            self.cursor.execute('SELECT * FROM user WHERE id=1')
            results = self.cursor.fetchall()[0]
            hash_passwd = results[3]
            b_passwd = passwd.encode('utf8')
            if bcrypt.checkpw(b_passwd, hash_passwd): return results
            else: return False
            # sql = """SELECT * FROM user WHERE passwd=?"""
            # self.cursor.execute(sql, (hash_passwd,))
            # records = self.cursor.fetchall()[0]
            # return records
        except: return False

    def create_credentials(self,access_key,secret_key,passwd) -> str:
        '''create new credentials in database'''

        salt = bcrypt.gensalt()
        hash_passwd = bcrypt.hashpw(passwd.encode('utf8'), salt)

        self.cursor.execute("INSERT INTO user(access_key,secret_key,passwd) VALUES(?, ?, ?);", (access_key,secret_key,hash_passwd))
        self.con.commit()
    
    def delete_db(self):
        sql = 'DROP TABLE user'
        self.cursor.execute(sql)
        self.con.commit()

    def close_connect(self):
        self.con.close()
        self.cursor.close()