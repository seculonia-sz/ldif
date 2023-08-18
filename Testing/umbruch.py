test_file = open("devk_dhcpd_vlan backup.ldif", "r") # ldif Datei wird eingelesen/geöffnet

liste = test_file.readlines() # Zeile für Zeile wird eingelesen

#print(liste[4-2]) # Print liste mit index [x]

zwischenspeicher = open("zwischenspeicher.txt", "w")

len_liste = len(liste) # Maximale Zeilen Länge
count=1
while count < 400: # Schleife von 1 bis 400 (Zeile für Zeile)
    len_line = len(liste[count].rstrip('\n')) # Länge einer einzelnen Zeile

   # Bedingung: Wenn 76 Zeichen enthalten sind
    if len_line == 76:
        new_line=liste[count].rstrip()+liste[count+1].rstrip() # Zusammengeführte Zeile mit der darauffolgenden
        
        print("--------------------------------------------------------------------", file=zwischenspeicher) # dummy
        print(count,new_line.replace(" ", ""), file=zwischenspeicher) # Ausgabe einer Zeile
        print(count,liste[count+1].rstrip(), file=zwischenspeicher) # Zweite Zahle
        print("===================================================================", file=zwischenspeicher) # dummy

        count=count+2 # Zähler (Überpsringt die Zusammengeführte Zeile)
    else: # Alle weiteren Zeilen die nicht 76 Zeichen lang sind sollen ausgegeben werden
        print(count,len_line,liste[count].rstrip().replace(" ", ""), file=zwischenspeicher) # Replace ersetzt leerstellen (indem die leerstellen entfernt werden)
        count=count+1 # Zähler

test_file.close() # Schließen der ldif datei
zwischenspeicher.close() # Schließen der zwischenspeicher.txt datei