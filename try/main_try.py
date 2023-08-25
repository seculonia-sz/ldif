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

    # jeder dn's eintrag
    for dns in dn_split:
        #print(dns[:3])
    # in dn's suche ou= (Die ersten 3 Zeichen werden überprüft)
        if dns[:3] == 'ou=':
            # wenn ou= vorhanden, überprüfe ob es ein Subnets ist (ab der dritten Stelle wird überprüft)
            if dns[3:] == 'Subnets':
                zeile+= "network"
                zeile+= "," + search_string('cn', record)
                net4 = ipaddress.ip_network(search_string('cn', record) + "/" + search_string('dhcpNetMask', record))
                zeile += "," + str(net4.netmask)

                # routers
                dhcp_option_split = search_string('dhcpOption', record).split(",")
                for dhcp_option in dhcp_option_split:
                    if dhcp_option[:7] == 'routers':
                        zeile+= "," + dhcp_option[8:] + "\n"

    
    #zeile+= search_string_cut('owner', record, 3, 0) + ","

# Die Zeile jeweils Komma separiert wird Ausgegeben, mit den einzelnen Werten aus der Datei
print(zeile)

# Als CSV Datei Speichern (FUNKTIONIERT)
csv_file = open("try/inhalt.csv", "w")
csv_file.writelines(zeile)
csv_file.close()

print ("--------------------------------------")
