zeile = str()

zeile += "Test,Test2"
zeile += "Jaguar,Tiger,Zebra,Affe,Bär,Puma,Löwe"

# csv
csv_file = open("function/data.csv", "a")
csv_file.write(zeile)
csv_file.writerow(zeile)
csv_file.close()