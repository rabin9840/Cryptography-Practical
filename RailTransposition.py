key=[4,3,1,2,5,6,7]
message="attackpostponeduntiltwoam"

def encrypt(key,message):
    cipherText=""
    remainingNoLetter=0
    matrixMessage=[[0]*len(key) for i in range(len(key))]
    print(matrixMessage)
    count=0
    totalRow=0

    if len(message)%len(key)!=0:
        remainingNoLetter=len(key)-len(message)%len(key)
        for x in range(0,remainingNoLetter):
            message+="x"
    
    totalRow=int(len(message)/len(key))

    #convert the matrix according to the key
    for i in range(len(key)):
        for j in range(len(key)):
            matrixMessage[i][j]=ord(message[count])
            count+=1
        if count==len(message):
            break

    #finding the position of key
    keyPosition=[[0] for i in range(len(key))]
    count=0
    for i in range(len(key)):
        for j in range(len(key)):
            if i==key[j]:
                keyPosition[count]=j
                break
        count+=1
    
    

    for i in range(len(keyPosition)):
        for j in range(totalRow):
            x=keyPosition[i]
            cipherText+=matrixMessage[j][x]
            
    
    print(cipherText)
    

encrypt(key, message)