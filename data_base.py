import psycopg2


class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='neondb',
            user='neondb_owner',
            password='npg_VC2NQ5BRmfhk',
            host='ep-wandering-leaf-ag4n7bd0-pooler.c-2.eu-central-1.aws.neon.tech',
            port=5432
        )
  
        self.cursor = self.conn.cursor()



    def get_users(self):
        self.cursor.execute('SELECT * FROM nasa_bot_users;')
        data = self.cursor.fetchall()
        return data

    def add_user(self, chat_id, username):
        self.cursor.execute('INSERT INTO nasa_bot_users(chat_id, username) VALUES(%s, %s)',(chat_id, username,))
        self.conn.commit()

    def get_users_by_id(self, chat_id):
        self.cursor.execute('SELECT * FROM nasa_bot_users WHERE chat_id = %s;', (chat_id,))
        self.conn.commit()

    def update_notification(self, noti_status,chat_id):
        self.cursor.execute('UPDATE nasa_bot_users SET noti_status = %s WHERE chat_id = %s;', (noti_status, chat_id,))
        self.conn.commit()

    def update_language(self, chat_id, language):
        self.cursor.execute('UPDATE nasa_bot_users SET language = %s WHERE chat_id = %s;', (language, chat_id,))
        self.conn.commit()

    def get_users_by_noti_status(self, noti_status):
        self.cursor.execute('SELECT * FROM nasa_bot_users WHERE noti_status = %s;', (noti_status,))
        self.conn.commit()


    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
