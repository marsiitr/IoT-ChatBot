import sqlite3


class db:

    def __init__(self):
        try:
            self.db = sqlite3.connect("user.sqlite")
            self.cursor = self.db.cursor()
            print('[result] Database connected!')

        except Exception as e:
            print('[error] error connecting database!')
            print(e)


    def add_user(self, username, password, first_name, last_name, email, phone_number):

        checkusername = self.cursor.execute(
            "SELECT username FROM users WHERE username=?", (username,))
        if checkusername is None:

            try:

                query = "insert into users (username, password, first_name, last_name, email, phone_number, last_login, api_key) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', now(), '{6}');".format(
                    username, password, first_name, last_name, email, phone_number, "api_key")
                # print(query)
                self.cursor.execute(query)
                self.db.commit()
                return True
            except Exception as e:
                print(e)
        else:
            return "USERNAME already exists"
