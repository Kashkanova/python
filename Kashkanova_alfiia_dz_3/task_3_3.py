
def thesaurus(*names):
    dict_names = {}
    for item in names:
        key = item[0]
        if key not in dict_names:
            dict_names[key]=[]
        dict_names[key].append(item)
    return dict_names
name = thesaurus("Иван", "Мария", "Петр", "Илья", "Света")
print(name)

