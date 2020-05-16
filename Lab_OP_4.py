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


name_file = "123.txt"
data = open("123.txt")
out = name_file.split(".")[0]
output_file = open(out + ".lzw", "w")
dict_size = 256
for s in data:
    print(s)
encoded = encoder(s, dict_size)
output_file.write(encoded)



print(encoded)
# output_file.write(encoded)
# decoded = decoder(encoded, dict_size)
# print(decoded)

# if len(argv) > 1:
#     formulaa = ""
#     for i in range(1, len(argv)):
#         formulaa = str(formulaa) + str(argv[i])
#
# else:
#     print("ERROR")


