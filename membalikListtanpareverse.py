def balikposisi(mylist):
    hasil =[]
    for i in range (len(mylist)):
        hasil.insert(0,mylist[i])
    return hasil
print(balikposisi(y))

print(60*'=')

x= ['andi','budi','caca']
y=[3,5,7,9]

def balikPosisi (mylist):
    for e in range(round(len(mylist)/2)):
        asli = mylist[e]
        mylist[e]= mylist[len(mylist)-1-e]
        mylist[len(mylist)-1-e]=asli
    return mylist
print(balikPosisi(y))