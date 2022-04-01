def encryption(code,plaintext):
    '''To encrypt the given plaintext to cipher text''' 
    cipherText=''
    for i in range(len(plaintext)):
        char=plaintext[i]

        if char.isupper():  #To encrypt the upper case letter
            cipherText=cipherText+code[char.lower()].upper()
            #we are first changing the upper case letter to lower case
            #to map the key of the letter in dictionary
            #then the key is changed to upper case

        elif char==' ':    #When space is present in the plain text
            cipherText=cipherText+char
        else:   #To encrypt the lower case letter
            cipherText+=code[char]
       
    return cipherText

def decryption(code,cipherText):
    '''To decrypt the cipher text to plain text'''
    
    plainText=''
    for i in range(len(cipherText)):
        #For upper case cipher text
        if cipherText[i].isupper():
            plainText=plainText+get_key(cipherText[i].lower()).upper()
        
        #When space is present in the cipher text
        elif cipherText[i] ==' ':
            plainText=plainText+cipherText[i]

        #For lower case cipher text
        else:
            plainText=plainText+get_key(cipherText[i])
        
    return plainText

def get_key(val): # used to get key using value from dict
    for key, value in code.items():
         if val == value:
             return key

normalChar = "abcdefghijklmnopqrstuvwxyz"
codedChar = "qwertyuiopasdfghjklzxcvbnm"
normalChar = list(normalChar)
codedChar=list(codedChar)

code={} # dict of normalChar and codedChar

for i in range(26):
    code[normalChar[i]]=codedChar[i]

plaintext=input("Please enter the plaintext to encrypt")
cipherText1=encryption(code,plaintext)
print(cipherText1)
plainText1=decryption(code,cipherText1)
print(plainText1)