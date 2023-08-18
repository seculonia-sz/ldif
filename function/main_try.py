from ldif import LDIFParser
from def_function import *

# Datei in der gelesen werden soll
datei = "Auslesen.ldif"

# LDIFparser
par= LDIFParser(open(datei, "rb"))

# -------------------- VERBESSERUNG --------------------
# - Die If bedingungen in eine Funktion umwandeln
# - doppelte, dreifache kommas entfernen
# - als csv datei speichern (spalten: überschriften darunter liegend die werte)
# - Weitere Werte abfragen bswp. objectClass, description, devktag, .........

for dn, record in par.parse():
    #print('got entry record: %s' % dn)
    #print(f"{record['o']}")


    # Zeile um alle spezifischen Inhalte dieser Zeile anzuhängen
    zeile = ''


    # Die Folgenden Überprüfungen Überprüfen die ldif datei ob ein bestimmter string
    # in dem Dictionary vorhanden ist. Ist das der Fall, so fügt die bedingung diesen
    # Wert dieses bestimmten Strings in die sogenannte "zeile" hinzu.

    # Überprüfe ob "cn" im record vorhanden ist (ldif datei)
    if 'cn' in record:
        #print("cn: "+record['cn'][0])      # Ergebnis 'cn' printen
        zeile += record['cn'][0] # Ergebnis 'cn' wird der Zeile hinzugefügt
    else: # Wenn ein neues ergebnis beginnt soll komma separiert werden
        zeile +=','

    # Überprüfe ob "owner" im record vorhanden ist (ldif datei)
    if 'owner' in record:
        #print("owner: "+record['owner'][0][3:]) # Ergebnis 'owner' printen
        zeile += ',' +record['owner'][0][3:] # Owner gibt als Ergebnis bswp den wert "dn=xyz" wo "dn=" nicht in das Ergebnis aufgenommen wird, daher ab der 3. Stelle soll die Zeile hinzugefügt werden
    else: # Wenn ein neues ergebnis beginnt soll komma separiert werden
        zeile +=','
 
    # Überprüfe ob "buisnessCategory" im record vorhanden ist (ldif datei)
    if 'businessCategory' in record:
        #print("owner: "+record['owner'][0][3:]) # Ergebnis 'buisnessCategorie' printen
        zeile += ',' +str(record['businessCategory']) # Ergebnis 'buisnessCategorie' wird der Zeile hinzugefügt
    else: # Wenn ein neues ergebnis beginnt soll komma separiert werden
        zeile +=','

    # ou
    # hosts
    # subnets
    # vlans
    # dhcp-pools

    zeile2=str()
    zeile2+= search_string('cn', record) + ","
    #zeile2+= search_string_cut('owner', record, 3, 1) + ","
    zeile2+= search_string_cut_test('owner', record, 3, 0) + ","
    zeile2+= search_string('businessCategory', record)
    print(zeile2)
    # Die Zeile jeweils Komma separiert wird Ausgegeben, mit den einzelnen Werten aus der Datei
    #print(zeile)

print ("--------------------------------------")
