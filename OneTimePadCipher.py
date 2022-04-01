#To encrypt and Decrypt the plain text to cipher Text and vice versa
import random as rd

def randomKeyGen():
    key=''
    for i in range(0,len(plainText)):
        key=key+chr(rd.randint(0,26)+97)
    return key

def numbering(s):
    numberlist=[]
    for i in range(0,len(s)):
        numberlist.append(ord(s[i])-97)
    return numberlist

def oneTimePadEncryption():
    cipherText=''
    message=numbering(plainText)
    keyEncp=numbering(randomkey)
    cipherInNumber=[]

    for i in range(0,len(message)):
        cipherInNumber.append((message[i]+keyEncp[i])%26)
        cipherText+=chr(cipherInNumber[i]+97)
    
    print('Cipher Text=',cipherText)
    
    return cipherInNumber

def oneTimePadDecrypt():
    cipher=oneTimePadEncryption()
    keyEncp=numbering(randomkey)
    plainafterdecrypt=''

    for i in range(0,len(cipher)):
        if (cipher[i]-keyEncp[i]<0):
            plainafterdecrypt+=chr(((cipher[i]-keyEncp[i]+26)%26+97))
        else:
            plainafterdecrypt+=chr((cipher[i]-keyEncp[i])%26+97)
    print("Plain Text After decryption=",plainafterdecrypt)


plainText=input("Enter the Plain Text to Encrypt And Decrypt")
randomkey=randomKeyGen()
print('key=',randomkey)
oneTimePadDecrypt()