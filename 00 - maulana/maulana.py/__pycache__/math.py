def generateKeys(string,key):
    key = list(key)
    if len(string) == len(key):
        return key
    else :
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("" . join(key))

def originalText(Cipher_Text,key):
    orig_text = []
    for i in range(len(Cipher_Text)):
        x = (ord(Cipher_Text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
        print("(",ord(Cipher_Text[i]),'-',ord(key[i]),"+ 26 )",' % ',26,"=",(ord(Cipher_Text[i]) - ord(key[i]) + 26) % 26)
    return ("" . join(orig_text))


string = "ECWMIUISWDSWVWGBRQPBOVEBXBRHOMTVNJZFWSXV"
keyword = "POLTEK"
key = generateKeys(string,keyword)
print("Original/Decrypted Text :",
        originalText(string , key))