import sys


def decode_char_from_key_char(cipher_char, key_char):
    rol_number = ord(key_char) - ord('a')
    
    chipher_alphabet_index = ord(cipher_char) - ord('a')
    rolled_cipher_index = (chipher_alphabet_index - rol_number) % 26
    return chr(rolled_cipher_index + ord('a'))


    
def decode_cipher(cipher_text, key):
    for cc, kc in zip(cipher_text, key):
        print(decode_char_from_key_char(cc, kc), end='')
        
        
decode_cipher(sys.argv[1], sys.argv[2])