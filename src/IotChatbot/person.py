from database import db
from datetime import datetime

class user:

    def __init__(self, username, password):
        self.db = db()
        self.username = username 
        self.secret = password
        self.authenticated = False
        self.auth()  

    def auth (self):
        #this is the place where user will get authenticated
        try:
            query = 'select password from users where username = "{0}"'.format(self.username)
            self.db.cursor.execute(query)
            output = self.db.cursor.fetchall()
            print(output[0][0])
            print(self.username)
            print(self.secret)
            if query is not None:
                if self.secret   == output[0][0]:
                    self.authenticated = True
                        
                    query = 'update users set last_login = now() where username = "{0}";'.format(self.username)
                    self.db.cursor.execute(query)
                    self.db.db.commit()

                    return True
            else:
                self.authenticated = False
                return False

        except Exception as e:
            print("[ERROR!]")
            print(e)
