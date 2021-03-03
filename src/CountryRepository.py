from DBconnection import DBconnection

class CountryRepository(DBconnection): 
    def findAll(self):
        db = DBconnection().getConnection()
        cursor = db.cursor()
        sql = "INSERT INTO countries_db (country, link) VALUES ('hungary', 'url')"
        cursor.execute(sql)
        db.commit()
        sql2 = "SELECT * FROM countries_db"
        cursor.execute(sql2)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

        

d = CountryRepository()
d.findAll() 