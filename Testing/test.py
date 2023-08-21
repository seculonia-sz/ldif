test_file = open("devk_dhcpd_vlan backup.ldif", "r")
liste = test_file.readlines()
test_file.close()

zwischenspeicher = open("zwischenspeicher.txt", "w")

len_liste = len(liste)
count = 1

while count < len_liste:
    len_line = len(liste[count].rstrip('\n'))

    if len_line == 76:
        new_line = liste[count].rstrip() + liste[count+1].rstrip()
        print(count, new_line, file=zwischenspeicher)
        count += 2
    else:
        line = liste[count].rstrip()
        if line:  # Falls man verwenden möchte Überprüfung nach Leeren Zeilen
            print(count, len_line, line, file=zwischenspeicher)
        count += 1

zwischenspeicher.close()