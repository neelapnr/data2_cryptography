def cesar_cipher(text, key):
    crypted_text = ""
    
    for char in text:
        crypted_text += chr (ord(char) + key) % 1_114_112

    return crypted_text

def cesar_uncipher(text, key):
    crypted_text = ""

    for char in text:
       crypted_text += chr ((ord(char) - key) % 1_114_112)

    return crypted_text 


