import sqlite3
username=input('Enter User name:')
password=input('Enter Password:')
sqliteConnection = sqlite3.connect('login.db')
cursor = sqliteConnection.cursor()
cursor.execute('''select uname password from log where uname=? and password=?;''',(username,password))
if not cursor.fetchone():
    print('login failed')
else:
    print('Welcome')
# cursor.execute('''create table log(uname varchar(10) NOT NULL, password varchar(10) NOT NULL)''')
# cursor.execute('''insert into log values('Vishnu','vishnu4625')''')
# cursor.execute('''insert into log values('Prasad','Prasad4625')''')
# cursor.execute('''delete from log''')
# sqliteConnection.commit()
# cursor.fetchall()
# print('Data inserted in the table:')
# data=cursor.execute('''select * from log''')
# for row in data:
#     print(row)
