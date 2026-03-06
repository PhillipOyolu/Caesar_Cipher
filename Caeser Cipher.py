message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
return_message = "Yes i was able to decode it,it was fun doing this. send me some more!"

def caeser_cipher(message, offset, decode=False):
    if decode:
        offset = -offset
    deciphered_message = ""
    for code in message:
        if code.isalpha():
            if code.isupper():
                base = ord("A")
            else:
                base = ord("a")
            position = ord(code) - base
            new_position = (position + offset) % 26
            new_char = chr(new_position + base)
            
            deciphered_message += new_char
        else:
            deciphered_message += code
            
    return deciphered_message

print(caeser_cipher(return_message, 10, True))