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

#def search_string_cut(str_search, record, frontcut=int, backcut=int):
#    wert = search_string(str_search, record)
#   wert_len = len(wert)
#backcut_result = wert_len - backcut
#    return wert[frontcut:backcut_result]


def search_string_cut_test(str_search, record, frontcut=int, backcut=int):
    wert = search_string(str_search, record)

    for werte in wert:
        print("-----------------------------")
        print(wert + " !GANZER STRING")

        wert_split = wert.split(",")
        for werte_ in wert_split:
            werte_len = len(werte_) - backcut
            print(werte_+ " !SCHLEIFEN WERT")
            print(werte_[frontcut:werte_len] + " !CUTTET_STRING")
            print("-----------------------------")
            return werte_[frontcut:werte_len]       
    