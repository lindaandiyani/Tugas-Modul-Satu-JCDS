def pangkatB(x,y):
    if (y==1):
        return x
    else:
        return x * pangkatB(x,y-1)
print(pangkatB(2,3))


pangkatB(2,3) = 2*pangkatB(2,2)      2*4 =8
pangkatB(2,3) = 2*pangkatB(2,1)      2*2 =4
pangkatB(2,3) = 2*pangkatB(2,0)      2*1 =2