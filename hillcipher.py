key="GYBNQKURP"
message="ACT"
keyMatrix=[[0]*3 for i in range(3)]


#Generate vector for matrix
messageVector=[[0] for i in range(3)]


#vector for result cipher 
cipherMatrix=[[0] for i in range(3)]

def getKeyMatrix(key):
    k=0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j]=ord(key[k])%65
            k+=1
    return keyMatrix

keymatrix=getKeyMatrix(key)


def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j]=0
            for x in range(3):
                cipherMatrix[i][j]+=(keyMatrix[i][x]*messageVector[x][j])
            cipherMatrix[i][j]=cipherMatrix[i][j]%26
    

def HillCipher(message,key):
    getKeyMatrix(key)

    #generate matrix for message
    for i in range(3):
        messageVector[i][0]=ord(message[i])%65
    print(messageVector)
    encrypt(messageVector)
    print(cipherMatrix)

    #Generate cipher text
    CipherText=[]
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0]+65))
    
    print(CipherText)

HillCipher(message, key)