from connection import Connection

conn = Connection.conn_local()
cur = conn.cursor()

print('Creating users table...')

create_users_table = """CREATE TABLE users (
    id serial PRIMARY KEY, username text UNIQUE, password text,
    first_name text NOT NULL, last_name text NOT NULL,
    birthday text NOT NULL, phone text, gender text,
    created_at timestamp NOT NULL, updated_at timestamp NOT NULL, deleted_at timestamp
)"""

cur.execute("select * from pg_class where relname = 'users'")
exists = cur.fetchone()
if exists:    
    print('Table already exist!')
else:
    cur.execute(create_users_table)
    print('Done!')
    

users = [
    {'username': 'pedro@gmail.com', 'password':'1234', 
    'first_name': 'Pedro', 'last_name': 'Cherubini', 'birthday':'00/00/0000','phone':'0000-0000','gender':'M'},
    {'username': 'milena@gmail.com', 'password':'1234',
    'first_name': 'Milena', 'last_name': 'Abade', 'birthday':'00/00/0000','phone':'0000-0000','gender':'F'},
    {'username': 'breno@gmail.com', 'password':'1234',
    'first_name': 'Breno', 'last_name': 'Yano', 'birthday':'00/00/0000','phone':'0000-0000','gender':'M'}
]

insert_query = """
    INSERT INTO users (username, password, first_name, last_name, birthday, phone, gender, created_at, updated_at) 
    VALUES (%(username)s, %(password)s, %(first_name)s, %(last_name)s, %(birthday)s, %(phone)s, %(gender)s, now(), now()) ON CONFLICT DO NOTHING;
    """

cur.executemany(insert_query, users)
print('row(s) inserted!')

conn.commit()
cur.close()
conn.close()


print('Creating products table...')

conn = Connection.conn_local()
cur = conn.cursor()

create_products_table = """CREATE TABLE products (
    id serial PRIMARY KEY, name text UNIQUE, code text UNIQUE, 
    description text,
    price numeric NOT NULL,
    created_at timestamp NOT NULL, updated_at timestamp NOT NULL, deleted_at timestamp
)"""

cur.execute("select * from pg_class where relname = 'products'")
exists = cur.fetchone()
if exists:    
    print('Table already exist!')
else:
    cur.execute(create_products_table)
    print('Done!')


products = [
    {'name': 'token1', 'code':'tz5590', 'price': 15.90},
    {'name': 'token2', 'code':'tz5591', 'price': 20.90},
    {'name': 'token3', 'code':'tz5592', 'price': 35.90}
]

insert_query = """
    INSERT INTO products (name, code, price, created_at, updated_at) 
    VALUES (%(name)s, %(code)s, %(price)s, now(), now()) ON CONFLICT DO NOTHING;
    """

cur.executemany(insert_query, products)
print('row(s) inserted!')

conn.commit()
cur.close()
conn.close()


print('Creating sold table...')

conn = Connection.conn_local()
cur = conn.cursor()

create_sold_table = """CREATE TABLE sold (
    id serial PRIMARY KEY, user_id int UNIQUE, product_id int UNIQUE, 
    quantity int,
    total_revenue numeric NOT NULL,
    created_at timestamp NOT NULL, updated_at timestamp NOT NULL
)"""

cur.execute("select * from pg_class where relname = 'sold'")
exists = cur.fetchone()
if exists:    
    print('Table already exist!')
else:
    cur.execute(create_sold_table)
    print('Done!')


revenue = [
    {'user_id':2 , 'product_id':3 ,'quantity':4 ,'total_revenue': 15.90},
    {'user_id':3 , 'product_id':1 ,'quantity':3 ,'total_revenue': 20.90},
    {'user_id':1 , 'product_id':2 ,'quantity':6 ,'total_revenue': 35.90}
]

insert_query = """
    INSERT INTO sold (user_id, product_id, quantity, total_revenue, created_at, updated_at) 
    VALUES (%(user_id)s, %(product_id)s, %(quantity)s, %(total_revenue)s, now(), now()) ON CONFLICT DO NOTHING;
    """

cur.executemany(insert_query, revenue)
print('row(s) inserted!')

conn.commit()
cur.close()
conn.close()