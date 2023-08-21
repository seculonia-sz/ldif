zwischenspeicher = open("zwischenspeicher.txt", "r")

def entferne_leerstellen(text):
    ohne_leerstellen = text.replace(" ", "")
    return ohne_leerstellen

ergebnis = entferne_leerstellen(zwischenspeicher)

print(ergebnis)
