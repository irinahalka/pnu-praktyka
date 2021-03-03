import mysql.connector
import ParsingContent 



db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password13",
    database = "coins"
)

curs = db.cursor()

#sql = "INSERT INTO countries_db (id, country, link) VALUES (%s, %s)"
sql = "SELECT * FROM countries_db"
curs.execute(sql)

myresult = curs.fetchall()

for x in myresult:
  print(x)

print(db)