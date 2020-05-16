from sys import argv


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


# data = open(str(argv[2]))
name_file=str(argv[2])
data = open(name_file)
dict_size = 256
print(data)
for s in data:
    print(s)


out = name_file.split(".")[0]
output_file = open(out + ".lzw", "w")


if str(argv[1]) == "e":
    encoded = encoder(s, dict_size)

    print(encoded)
    output_file.write(str(encoded))
# elif str(argv[1])=="d":
#     decoded = decoder(encoded, dict_size)
#     print(decoded)



