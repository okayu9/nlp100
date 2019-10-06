def cipher(string):
    return ''.join(map(cipher_char, string))


def cipher_char(char):
    if char.islower():
        return chr(219 - ord(char))
    else:
        return char


original_sentence = 'I am an NLPer'

ciphered_sentence = cipher(original_sentence)
print(ciphered_sentence)

deciphered_sentence = cipher(ciphered_sentence)
print(deciphered_sentence)
