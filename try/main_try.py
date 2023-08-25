from ldif import LDIFParser
from def_function import *
import ipaddress

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
test = 1

# Header
header = "header-network,address,netmask,routers\n"

# Erstellen der Zeilen (als String) # Ihalte dieser Zeile anzuhängen
zeile=str()

# Header hinzufügen 
zeile += header
for dn, record in par.parse():
    # Inhalte
    #zeile+= dn + ","
    dn_split = dn.split(",")

    for dns in dn_split:
        #print(dns[:3])
        if dns[:3] == 'ou=':
            if dns[3:] == 'Subnets':
                zeile+= "network"
                zeile+= "," + search_string('cn', record)
                net4 = ipaddress.ip_network(search_string('cn', record) + "/" + search_string('dhcpNetMask', record))
                zeile += "," + str(net4.netmask) + "\n"
                #zeile += search_string('cn', record)

    
    #zeile+= search_string_cut('owner', record, 3, 0) + ","

# Die Zeile jeweils Komma separiert wird Ausgegeben, mit den einzelnen Werten aus der Datei
print(zeile)

# Als CSV Datei Speichern (FUNKTIONIERT)
csv_file = open("try/inhalt.csv", "w")
csv_file.writelines(zeile)
csv_file.close()

print ("--------------------------------------")
