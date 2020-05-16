def decoder(data, dict_size):
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    lst = []
    str = chr(data.pop(0))
    lst.append(str)
    for key in data:
        if key in dictionary:
            entry = dictionary[key]
        elif key == dict_size:
            entry = str + str[0]
        lst.append(entry)
        dictionary[dict_size] = str + entry[0]
        dict_size += 1
        str = entry
    s = ''
    for i in range(len(lst)):
        s = s + lst[i]
    return s


name_file = str(argv[2])
data = open(name_file)
dict_size = 256
print(decoder(data, dict_size))
