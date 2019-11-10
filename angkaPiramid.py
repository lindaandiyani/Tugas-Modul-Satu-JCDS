def angkaPiramid(x):
    output = ''
    for i in range (x):
        for j in range(i):
            print(j + 1, end=' ')
        print()
            
    return output
angkaPiramid(6)

def angkakebalik(c):
    output=''
    for i in range(c):
        for j in range(0,c-i):
            print(j+1,end=' ')
        print()
    return output
angkakebalik(5)
print()
def angkakembar(d):
    output=''
    for i in range(d+1):
        print(str(i)*i,end=' ')
        print()
angkakembar(5)
print()
def angkaKembarkebalik (e):
    for i in range(1,e+1):
        print(str(i)*(e-i),end=' ')
        print()
angkaKembarkebalik(6)
print()
def urutanMundur(e):
    for i in range(e,0,-1):
        print(str(i)*(e-i),end=' ')
        print()
urutanMundur(6)
print()
def urutankebalik(g):
    for i in range(g,0,-1):
        print(str(i)*(g),end=' ')
        g-=1
        print()
urutankebalik(5)