str_name = "dc=produktion,dc=vorproduktion"

result = str_name.split(",")
for results in result:
    cut = results[3:]
    print(cut)
print(result)