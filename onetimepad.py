#To encrypt and Decrypt the plain text to cipher Text and vice versa
import random as rd

def randomKeyGen():
    ''' Generate the random key matching the length of the plain text. '''
    key=''
    for i in range(0,len(plainText)):
        key=key+chr(rd.randint(0,26)+97)
    return key


def numbering(s):
    ''' To number the given string by finding the character integer value and subtracting from base value.'''
    numberlist=[]
    for i in range(0,len(s)):
        numberlist.append(ord(s[i])-97)
    return numberlist
    

def oneTimePadEncryption():
    ''' Encrypt the given text using OneTimePad Encryption.'''
    cipherText=''
    message=numbering(plainText)
    keyEncp=numbering(randomkey)

    for i in range(len(message)):
        if plainText[i]==' ':
            cipherText=cipherText+plainText[i]
        else:   
            cipherText+=chr((((message[i]+keyEncp[i])%26)+97))
    print('Cipher Text=',cipherText)
    
    return cipherText

#Optional for encryption else part
#cipherText+=chr((((ord(plainText[i])-97+ord(randomjey[i])-97)%26)+97))
#here no need to define numbering function



def oneTimePadDecrypt():
    '''To Decrypt the given Cipher Text'''
    cipherText=oneTimePadEncryption()
    cipher=numbering(cipherText)
    keyEncp=numbering(randomkey)
    plainafterdecrypt=''

    for i in range(0,len(cipher)):
        if cipherText[i]==' ':
            plainafterdecrypt+=cipherText[i]
        else:
            plainafterdecrypt+=chr(((cipher[i]-keyEncp[i])+26)%26+97)

    print("Plain Text After decryption=",plainafterdecrypt)


plainText=input("Enter the Plain Text to Encrypt And Decrypt:")
randomkey=randomKeyGen()
print('key=',randomkey)
oneTimePadDecrypt()