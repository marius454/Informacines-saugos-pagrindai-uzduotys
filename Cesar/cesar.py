
coded_word = "ZP CPZ WHJLT WHYH ILSSBT"

values = list()
for char in coded_word:
    if char != ' ':
        values.append(ord(char) - 65)
    else:
        values.append(ord(char))


for i in range(1,26):
    decoded_chars = list()
    for value in values:
        if value < 26:
            decoded_value = (value - i + 26) % 26
            decoded_chars.append(chr(decoded_value + 65))
        else:
            decoded_chars.append(chr(value))

    print (''.join(decoded_chars), i)
    
