import mysql.connector as connection

mydb= connection.connect(host="localhost", user= "root", password= "Nitish@2503")
print(mydb)
cursor = mydb.cursor()
cursor.execute("create table nitish.nitishdetails(name varchar(10), mail_id varchar(20), roll_no int(10))")
