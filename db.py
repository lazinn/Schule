import mysql.connector

mydb = mysql.connector.connect(
  host="datenbank.goofyatzen.de",
  user="python",
  password="test",
  database="Test"
)

mycursor = mydb.cursor()

sql = "UPDATE `fahrrad` SET `Bezeichnung` = 'REACTION HYBRID ABS 75' WHERE `fahrrad`.`ArtikelID` = 1"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
