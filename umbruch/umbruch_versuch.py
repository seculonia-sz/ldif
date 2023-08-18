test_file = open("test.txt", "r")

lines = test_file.readlines()

# Count Lines
line_counter = 0
# Correct Counter
correct_chars = 0

# Prints
print("--- SUCHE ---")
print("Suche nach Zeilen mit 3 oder mehr Zeichen...\n")

# Schleife für Zeilen in der test_file datei
for line in lines:
    line_counter+=1
    max_lines = len(lines)
    chars = len(line)-1

    # Überprüfung 3 oder mehr Zeichen
    if chars >= 3:
        print(f"in Zeile {line_counter}, gefunden:")
        print(f"Inhalt: {line}")
        #print(f"Inhalt Nächster Zeile: {line+1}")

        change_line = str(input("Soll dieser Zeile das letzte Zeichen entfernt werden? y/n\n"))
        if change_line == "y":
            print("OKAY")
        elif change_line == "n":
            print("NICHT OKAY")
        else:
            print("NICHT OKAY")
    else:
        correct_chars+=1

print("\n\n\n")
print(f"Maximale Anzahl Zeilen in der Datei: {max_lines}")
print(f"Anzahl Zeilen die Unter 3 Zeichen besitzen: {correct_chars}")

test_file.close()