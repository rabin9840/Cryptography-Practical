#Python Program to Encrypt and Decrypt the given Plain Text.

plainText=input("Enter the plain Text to Encrypt: ").lower()
key=input('Enter the key: ')
plainTextLength=len(plainText)
KeyLength=len(key)

def numbering(s):
    '''
    To convert the string to its number and return it as a list of number
    '''
    plainnumber=[]
    for i in range(0,len(s)):
        plainnumber.append(ord(s[i])-97)
    return plainnumber


def CreateNewKey():
    ''' To create a key that match the length of the plaintext. 
        Returns the number of the new key.'''
    newkey=key
    if plainTextLength>=KeyLength:
        for i in range(KeyLength,plainTextLength):#start to append the new key from the beginnig of the length of key to plaintext length
            newkey+=key[i%KeyLength]#to match the key length
    else:
        print("The key length is greater than the text")
    newKeyNumber=numbering(newkey)
    return newKeyNumber




def vigenereEncryption():
    ''' To Encrypt the plaintext to CipherText.
        Returns the number of cipher text obtained after adding numbers of plainText and key.'''
    cipherText=''
    message=numbering(plainText)    #store the number of plainText
    keyEncp=CreateNewKey()          #store the numbering of key
    cipherInNumber=[]

    for i in range(plainTextLength):
        cipherInNumber.append((message[i]+keyEncp[i])%26)   #store the number otained adding plaintext and key number.
        cipherText+=chr((cipherInNumber[i]+97))             #to convert the obtained number to its character form.
    print(cipherText)

    return cipherInNumber
    
    


def vigenereDecyption():
    ''' To decrypt the cipher text to its original PlainText.'''
    cipher=vigenereEncryption()
    keyEncp=CreateNewKey()
    plainafterdecrypt=''

    for i in range(0,len(cipher)):
        if (cipher[i]-keyEncp[i])<0:
            plainafterdecrypt+=chr(((cipher[i]-keyEncp[i])+26)%26+97)
            
        else:
            plainafterdecrypt+=chr((cipher[i]-keyEncp[i])%26+97)
    print(plainafterdecrypt)




vigenereDecyption()
