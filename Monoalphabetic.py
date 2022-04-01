def encryption(plain_text,code):
    ''' To encrypt the plain text'''
    plain_text.lower()
    cipher_text=''
    for i in range(len(plain_text)):
        #if plain_text[i]==' ':.
        #    cipher_text+=plain_text[i]
        if plain_text[i].islower():
            #here we are using code dictionary to map the plain text to its cipher text
            cipher_text+=code[plain_text[i]]
        else:
            plain_text[i].lower()
            cipher_text+=code[plain_text[i]]
    return cipher_text
        
#def decryption(cipherText,code):
#    '''To decrypt the cipher text'''
#    plainText=''
#
#    for i in range(len(cipherText)):
#        if cipherText[i]==' ':
#            plainText+=cipherText[i]
#        else:
#            plainText+=get_key(cipherText[i])
#    return plainText

def get_key(val):
    '''Use to get key from the dictionary of key'''
    for key,value in code.items():
        if val==value:
            return key

normalChar = "abcdefghijklmnopqrstuvwxyz"
codedChar = "qwertyuiopasdfghjklzxcvbnm"
normalChar = list(normalChar)
codedChar=list(codedChar)

code={} # dict of normalChar and codedChar
for i in range(26):
    code[normalChar[i]]=codedChar[i]

plaintext='hello World'
cipherText1=encryption(plaintext,code)
print(cipherText1)
#plainText1=decryption(cipherText1,code)
#print(plainText1)




