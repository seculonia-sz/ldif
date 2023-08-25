def search(str_search, record):
    if str_search in record:
        #print(f"Funktiontest: {str_search}: " + record[str_search][0])
        return record[str_search]
    else:
        return False
        
def search_string(str_search, record):
    wert = search(str_search, record)
    if wert:
        return ','.join(wert)
    else:
        return ','

# Suche nach einem String, schneidet vorne und/oder hinten Zeichen ab
def search_string_cut(str_search, record, frontcut=int, backcut=int):
    wert = search_string(str_search, record)
    wert_split = wert.split(",")
    counter = 0
    for werte_ in wert_split:
        werte_len = len(werte_) - backcut
        wert_split[counter] = werte_[frontcut:werte_len]
        counter+=1
    return ','.join(wert_split)

# ALTE funktion: Suche nach einem String, schneidet vorne und/oder hinten Zeichen ab
#def search_string_cut(str_search, record, frontcut=int, backcut=int):
#    wert = search_string(str_search, record)
#   wert_len = len(wert)
#backcut_result = wert_len - backcut
#    return wert[frontcut:backcut_result]
    