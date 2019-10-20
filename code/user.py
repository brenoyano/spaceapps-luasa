from connection import Connection



class User(object):

    @classmethod
    def log_in_user(cls, username, password):
        conn = Connection.conn_local()
        cur = conn.cursor()
        username = {'username': username, 'password': password}
        get_user = """
            select * from users where username = %(username)s
            and password = %(password)s;
            """
        result = cur.execute(get_user, username)
        row = cur.fetchone()
        if row:
            user = row
        else:
            user = None
        
        cur.close()
        conn.close()
        return user


    @classmethod
    def email_exist(cls, username):
        conn = Connection.conn_local()
        cur = conn.cursor()
        username = {'username': username}
        get_user = """
            select * from users where username = %(username)s;
            """
        result = cur.execute(get_user, username)
        row = cur.fetchone()
        if row:
            user = row
        else:
            user = None
        
        cur.close()
        conn.close()
        return user

    
    def create_user(self, username, password, first_name,last_name,birthday,phone,gender):
        conn = Connection.conn_local()
        cur = conn.cursor()
        username = {'username': username, 'password': password, 
        'first_name': first_name, 'last_name': last_name, 'birthday':birthday,'phone':phone,'gender':gender}
        insert_user = """
    INSERT INTO users (username, password, first_name, last_name, birthday, phone, gender, created_at, updated_at) 
    VALUES (%(username)s, %(password)s, %(first_name)s, %(last_name)s, %(birthday)s, %(phone)s, %(gender)s, now(), now()) ON CONFLICT DO NOTHING;
    """
        cur.execute(insert_user, username)
        
        conn.commit()
        cur.close()
        conn.close()
        print('User Created!')