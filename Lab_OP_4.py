from sys import argv


def encoder(data, dict_size):
    dictionary = dict((chr(i), i) for i in range(dict_size))
    string = ""
    lst = ''
    for symbol in data:
        ss = string + symbol
        if ss in dictionary:
            string = ss
        else:
            lst = lst + str(dictionary[string]) + ' '
            dictionary[ss] = dict_size
            dict_size += 1
            string = symbol
    if string:
        lst = lst + str(dictionary[string]) + ' '
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


def parse_file(text):
    result_list = []
    for line in text:
        numbs = line.split()
    result_list.append(numbs)
    return result_list


if argv[1]=="e":
    name_file = str(argv[2])
    data = open(name_file)
    out = name_file.split(".")[0]
    output_file = open(out + ".lzw", "w")
    dict_size = 256
    for s in data:
        print(s)
    encoded = encoder(s, dict_size)
    output_file.write(encoded)
    print(encoded)
if argv[1]=="d":
    dict_size = 256
    name_file=str(argv[2])
    data = open(name_file)
    for s in data:
        print(s)
    encoded=s.split()
    print(encoded)
    for i in range(len(encoded)):
        encoded[i]= int(encoded[i])
    decoded = decoder(encoded, dict_size)
    print(decoded)
    out = name_file.split(".")[0]
    output_file = open(out + ".txt", "w")
    output_file.write(decoded)


