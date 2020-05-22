from sys import argv
from struct import *
from config import *


def Encode(data, dict_s):
    dictE = {chr(i): i for i in range(dict_s)}
    string = ""
    for symb in data:
        string_plus_symbol = string + symb
        if string_plus_symbol in dictE:
            string = string_plus_symbol
        else:
            comp_data.append(dictE[string])
            dictE[string_plus_symbol] = dict_s
            dict_s = dict_s + 1
            string = symb
    if string in dictE:
        comp_data.append(dictE[string])
    return comp_data


def read_comp_file(file):
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data,) = unpack('>H', rec)
        comp_data.append(data)
    return comp_data


def Decode(n_code, comp_data,string):
    dictD = dict([(x, chr(x)) for x in range(dict_s)])
    decomp_data = ""
    for code in comp_data:
        if code in dictD:
            pass
        else:
            dictD[code] = string + (string[0])
        decomp_data += dictD[code]
        if len(string) == 0:
            pass
        else:
            dictD[n_code] = string + (dictD[code][0])
            n_code += 1
        string = dictD[code]
    return decomp_data


if argv[1] == "e":
    input_file = argv[2]
    file = open(input_file)
    data = file.read()
    out = input_file.split(".")[0]
    output_file = open(out + ".lzw", "wb")
    comp_data = Encode(data, dict_s)
    for data in comp_data:
        output_file.write(pack('>H', int(data)))
    output_file.close()
    file.close()
if argv[1] == "d":
    input_file = argv[2]
    file = open(input_file, "rb")
    out = input_file.split(".")[0]
    output_file = open(out + ".txt", "w")
    comp_data = read_comp_file(file)
    string = ''
    decomp_data = Decode(n_code, comp_data,string)
    for data in decomp_data:
        output_file.write(data)
    output_file.close()
    file.close()
