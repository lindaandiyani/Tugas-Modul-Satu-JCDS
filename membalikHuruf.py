inputKalimat =input('maskkan kalimatmu disini :')

def getReverse(kalimat):
    outputan=''
    listkata=inputKalimat.split(' ')
    for kata in listkata:
        outputan += kata[::-1] + ' '
    return outputan
    print(f'hasil balikan :{outputan}')
print(getReverse(inputKalimat))

