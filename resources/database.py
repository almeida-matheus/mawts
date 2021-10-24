import sqlite3
import bcrypt

class Database:

    def __init__(self,db_credentials) -> str:
        '''constructor to create curso to connecta to db and create a table with credentials if not exist'''
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
        '''scan database to get values'''
        self.cursor.execute('SELECT * FROM user WHERE id=1')
        result = self.cursor.fetchall()
        if result: return True
    
    def get_credentials(self,passwd=None):
        '''scan database to get values'''
        try:
            sql = """SELECT * FROM user WHERE passwd=?"""
            self.cursor.execute(sql, (passwd,))
            records = self.cursor.fetchall()
            return records[0]
        except:
            return False

    def create_credentials(self,access_key,secret_key,passwd) -> str:
        '''create new credentials in database'''
        self.cursor.execute("INSERT INTO user(access_key,secret_key,passwd) VALUES(?, ?, ?);", (access_key,secret_key,passwd))
        self.con.commit()
    
    def delete_db(self):
        sql = 'DROP TABLE user'
        self.con.commit()

    def close_connect(self):
        self.con.close()
        self.cursor.close()