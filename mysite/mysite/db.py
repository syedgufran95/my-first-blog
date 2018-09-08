import mysql.connector
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123123100',
    database='db1',
    auth_plugin='mysql_native_password'

)
mycursor=mydb.cursor()
mycursor.execute("SELECT *FROM student")
myresult=mycursor.fetchall()
for row in myresult:
    print(row)
mydb.commit()