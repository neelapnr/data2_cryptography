def cesar_cipher(text, key):
    crypted_text = ""
    
    for char in text:
        crypted_text += chr (ord(char) + key)

    return crypted_text

print(cesar_cipher("chocolat", 25))

