from ldif import LDIFParser
from def_function import *

# Datei in der gelesen werden soll
datei = "Auslesen.ldif"

# LDIFparser
par= LDIFParser(open(datei, "rb"))

# -------------------- PLANUNG --------------------
# - aus dn's stuktur aufbauen:
#   - in ou:
    # hosts
    # subnets
    # vlans
    # dhcp-pools
# - als csv datei speichern (spalten: überschriften darunter liegend die werte)

for dn, record in par.parse():
    # Erstellen der Zeilen (als String) # Ihalte dieser Zeile anzuhängen
    zeile=str()

    # Inhalte
    zeile+= dn + ","
    # TEST
    if 'ou' in dn:
        print('ou' in dn)

    zeile+= search_string('cn', record) + ","
    zeile+= search_string_cut('owner', record, 3, 0) + ","
    zeile+= search_string('businessCategory', record) + ","

    # Die Zeile jeweils Komma separiert wird Ausgegeben, mit den einzelnen Werten aus der Datei
    #print(zeile)

    # Als CSV Datei Speichern (FUNKTIONIERT)
    #csv_file = open("try/inhalt.csv", "a")
    #csv_file.write(zeile + "\n")
    #csv_file.close()

print ("--------------------------------------")
