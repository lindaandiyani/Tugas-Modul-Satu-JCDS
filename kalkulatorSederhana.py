def calc():
    angka1 = int(input('masukkan angka pertama : '))
    arit = input('masukkan operator aritmatika :')
    angka2= int(input('masukkan angka kedua : '))
    if arit == '/':
        print(angka1/angka2 )
    elif arit == '+':
        print(angka1+angka2)
    elif arit == '-':
        print(angka1-angka2)
    elif arit == '*':
        print(angka1*angka2)
    else:
        print('operator belum diketahui')
calc()