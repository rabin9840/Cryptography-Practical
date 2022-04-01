#HERE ASCII VALUE OF BASE A IS 65 AND a is 97 which we are directly subtracting in the function
def encryption(text,shift):
    ''' To encrpt the given text using Caesar Cipher'''

    cipherText=""
    
    #To traverse the each letter in the text
    for i in range(len(text)):
        #each character of text
        char=text[i]
        
        #encrypt uppercase
        if char.isupper():
            cipherText+=chr((ord(char)+shift-65)%26+65)

        #When there is space present in the plain text no change 
        elif char==" ":
            cipherText+=char
        
        #encrypt the lowercase letter
        else:
            cipherText+=chr((ord(char)+shift-97)%26+97)
            
    return cipherText



def decryption(text,key):
    '''To decrypt the cipher text to plain text'''

    plainText=""

    for i in range(len(text)):
        cipherText=text[i]

        #decrypt the upperletter
        if cipherText.isupper():
            plainText+=chr((ord(cipherText)-key-65)%26+65)

        elif cipherText==" ":
            plainText+=cipherText

        #decrypt the lowercase letter
        else:
            plainText+=chr((ord(cipherText)-key-97)%26+97)
    return plainText
        



print(encryption("ABC Def", 3))


#decryption using same encryption function where we send the shift value as
#shift=26-key
print(encryption("DEF def",23))

print(decryption("def ghi", 3))




