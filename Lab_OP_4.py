def encoder(data, dict_size):
    dictionary = dict((chr(i), i) for i in range(dict_size))
    str = ""
    lst = []
    for symbol in data:
        ss = str + symbol
        if ss in dictionary:
            str = ss
        else:
            lst.append(dictionary[str])
            dictionary[ss] = dict_size
            dict_size += 1
            str = symbol
    if str:
        lst.append(dictionary[str])
    return lst

name_file=str(argv[2])
data = open(name_file)
dict_size = 256
print(data)
for s in data:
    print(s)
print(encoder(s,dict_size))
    