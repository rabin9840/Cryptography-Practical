#for 2 rails:
text='Youareataparty'
plainText=text.strip()
length=len(plainText)


cipherText=''

def railFenchEncryption():
    railFenchText1=''
    railFenchText2=''
    for i in range(0,length):
        if i%2==0:
            railFenchText1+=plainText[i]
        else:
            railFenchText2+=plainText[i]
    cipherText=railFenchText1+railFenchText2
    print("Cipher Text="+cipherText)
    return cipherText



def railFenchDecrypt():
    railFenchTextDecrypt1=''
    railFenchTextDecrypt2=''
    txt=''
    cipehrTextecnrypt=railFenchEncryption()
    if len(cipehrTextecnrypt)%2!=0:
        lengt=int(len(cipehrTextecnrypt)/2+1)
    else:
        lengt=int(len(cipehrTextecnrypt)/2)
    
    railFenchTextDecrypt1=cipehrTextecnrypt[0:lengt]
    railFenchTextDecrypt2=cipehrTextecnrypt[lengt:length]
    
    for i in range(0,lengt):
        txt+=railFenchTextDecrypt1[i]
        if len(cipehrTextecnrypt)%2!=0 and i==lengt-1:
            break;
        txt+=railFenchTextDecrypt2[i]
    print(f"The plain Text after Decryption is {txt}")


railFenchDecrypt()

        

