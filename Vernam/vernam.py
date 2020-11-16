string = "Marius"
coded_string = "00011011000111100001101100011011000110100101001100110010000000000001100000011101000110010000111100011010"
key = "01001001011001110110111101110010011010010111001101100010011001010110110001101111011101100110000101110011"
print (len(key))


def encode(string, key):
    byte_array = bytearray(string, "ascii")

    byte_list = list()
    string_byte_list = list()

    for byte in byte_array:
        binary = bin(byte)
        byte_list.append(binary)
        string_binary = str(binary)[2:]
        while len(string_binary) < 8:
            string_binary = "0" + string_binary
        string_byte_list.append(string_binary)

    binary_string = "".join(string_byte_list)
    my_key = key[:len(binary_string)]

    coded_string = ""
    for i in range(len(binary_string)):
        if binary_string[i] == my_key[i]:
            coded_string += "0"
        else:
            coded_string += "1"

    print (my_key)
    print (binary_string)
    print (coded_string)

def decoode(string, key):
    my_key = key[:len(string)]
    print (len(string))
    decoded_binary = ""
    for i in range(len(string)):
        if string[i] == "0":
            decoded_binary += my_key[i]
        else:
            if my_key[i] == "0":
                decoded_binary += "1"
            else:
                decoded_binary += "0"

    print (my_key)
    print (decoded_binary)
    print (string)

    n = 8
    temp = [decoded_binary[i:i+n] for i in range(0, len(decoded_binary), n)]
    decoded_binary = " ".join(temp)
    print (decoded_binary)

# decoode(coded_string, key)
encode(string, key)