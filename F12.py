import mysql.connector

mydb = mysql.connector.connect(
  host="datenbank.goofyatzen.de",
  user="python",
  password="test",
  database="Fahrrad"
)

Hersteller = "Test"
bezeichnung = "Schulpräsi"
Beschreibungstext = "guter akku"
Listenpreis = 999.00
Rahmenhöhe = "27"
Gewicht = 19.00
Schaltungstyp = "Kettenschaltung"
Bremsentyp = "Scheibenbremse"
farbe = "schwarz"
Fahrradtyp = "3"

mycursor = mydb.cursor()

# Constructing the long description
lang_bezeichnung = Hersteller + " " + bezeichnung + ", " + farbe + ", " + Rahmenhöhe

# Inserting into the 'fahrrad' table
fahrrad_einfuegen = """
Insert INTO fahrrad (Hersteller, Bezeichnung, lang_bezeichnung, Beschreibungstext, Listenpreis)
Values (%s, %s, %s, %s, %s)
"""

mycursor.execute(fahrrad_einfuegen, (Hersteller, bezeichnung, lang_bezeichnung, Beschreibungstext, Listenpreis))

# Committing the insert to get the ArtikelID
mydb.commit()

# Fetching the inserted row's ID
ID_abfrage = "Select ArtikelID from fahrrad where lang_bezeichnung = %s"
mycursor.execute(ID_abfrage, (lang_bezeichnung,))
id = mycursor.fetchone()[0]  # Extracting the actual ID from the tuple

# Inserting into the 'fahrradmerkmale' table
fahrradmerkmale = """
Insert INTO fahrradmerkmale (ArtikelID, Rahmenhöhe, Gewicht, Schaltungstyp, Bremsentyp, farbe, FahrradtypID)
Values (%s, %s, %s , %s, %s, %s, %s)
"""

mycursor.execute(fahrradmerkmale, (id, Rahmenhöhe, Gewicht, Schaltungstyp, Bremsentyp, farbe, Fahrradtyp))

# Committing the insert
mydb.commit()

print(mycursor.rowcount, "record(s) affected")
