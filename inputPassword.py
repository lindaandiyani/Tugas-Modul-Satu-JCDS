password = '12345'
inputuser = ''
jumlahinput = 0
batasinput= 5
lebih = False  

while inputuser != password and not lebih:
    if jumlahinput< batasinput:
        inputuser = input (f'input ke-  {jumlahinput +1} ketikkan password : ')
        jumlahinput +=1
    else:
        lebih = True
if lebih:
    print('kesempatan habis, tunggu 24 jam')
else:
    print('password anda benar')