def prima(x):
    a= False
    if x > 1:
        if x == 2:
            a= True
        else :
            for i in range(2,x):
                if x %i == 0:
                    a= False
                    break
                else:
                    a= True
    else:
        a= False
    return a
print(prima(2))

z = list (filter(prima,range(101)))
print(z)