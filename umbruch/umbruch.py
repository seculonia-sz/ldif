test_file = open("devk_dhcpd_vlan backup.ldif", "r") # ldif Datei wird eingelesen/geöffnet

liste = test_file.readlines() # Zeile für Zeile wird eingelesen

#print(liste[4-2])

len_liste = len(liste) # Maximale Zeilen Länge
count=1
while count < 400: # Schleife von 1 bis 400 (Zeile für Zeile)
    print("#",count) # dummy
    #print(count)
    #print(liste[count])

    len_line = len(liste[count].rstrip('\n')) # Länge einer einzelnen Zeile
    #print(liste)
   # print(len_line, liste[count].rstrip('\n'))

   # Bedingung: Wenn 76 Zeichen enthalten sind
    if len_line == 76:
        new_line=liste[count].rstrip()+liste[count+1].rstrip() # Zusammengeführte Zeile mit der darauffolgenden
        print("--------------------------------------------------------------------") # dummy
        print(count,new_line) # Ausgabe einer Zeile
        print(count,liste[count+1].rstrip()) # Zweite Zahle
        print("===================================================================") # dummy
        count=count+2 # Zähler (Überpsringt die Zusammengeführte Zeile)
        print("##",count) # dummy
    else: # Alle weiteren Zeilen die nicht 76 Zeichen lang sind sollen ausgegeben werden
        print(count,len_line,"=>",liste[count].rstrip()) # Die Pfeile dienen nur der Orientierung
       
        print("###",count) # dummy
        count=count+1 # Zähler