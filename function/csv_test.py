zeile = str()

zeile += "Test,Test2\n"
zeile += "Jaguar,Tiger,Zebra,Affe,Bär,Puma,Löwe\n"

# csv
csv_file = open("function/data.csv", "a")
csv_file.write(zeile)
csv_file.writerow(zeile)
csv_file.close()