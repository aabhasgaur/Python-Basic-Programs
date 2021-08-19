def rotatedWords(cls, input1,input2):
    rotateString = input1.split(' ')
    count = 0
    for i in range(1,input2+1):
        for j in range(len(rotateString)):
            rotateString[j]= rotateString[j][1:]+rotateString[j][0]

    actualWrod = input1.split(' ')

    for i in range(len(rotateString)):
        for j in range(len(actualWrod)):
            if rotateString[i]==actualWrod[j]:
                count+=1
    return count

print(rotatedWords(1,"adaada",3))
print(rotatedWords(1,"llohe ereth",2))
