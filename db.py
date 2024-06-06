import mysql.connector

mydb = mysql.connector.connect(
  host="datenbank.goofyatzen.de",
  user="python",
  password="test",
  database="Test"
)

Hersteller="Test"
bezeichnung="keta"
Beschreibungstext="guter akku"
Listenpreis=999.00
Rahmenhöhe="27"
Gewicht=19.00
Schaltungstyp="Kettenschaltung"
Bremsentyp="Scheibenbremse"
farbe="schwarz"
Fahrradtyp="3"

mycursor = mydb.cursor()

lang_bezeichnung= Hersteller + " " + bezeichnung + ", " + farbe + ", " + Rahmenhöhe

fahrrad_einfuegen = "Insert INTO fahrrad (Hersteller, Bezeichnung, lang_bezeichnung, Beschreibungstext, Listenpreis) Values (%s, %s, %s, %s, %s)"

mycursor.execute(fahrrad_einfuegen, (Hersteller, bezeichnung, lang_bezeichnung, Beschreibungstext, Listenpreis))

ID_abfrage = "Select ArtikelID from fahrrad where lang_bezeichnung = %s"

mycursor.execute(ID_abfrage, (lang_bezeichnung,))
id = mycursor.fetchone()

fahrradmerkmale = "Insert INTO fahrradmerkmale (ArtikelID, Rahmenhöhe, Gewicht, Schaltungstyp, Bremsentyp, farbe, FahrradtypID) Values (%s, %s, %s , %s, %s, %s, %s)"
mycursor.execute(fahrradmerkmale, (id, Rahmenhöhe, Gewicht, Schaltungstyp, Bremsentyp, farbe, Fahrradtyp))

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
