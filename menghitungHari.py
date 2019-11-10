hari =['senin', 'selasa','rabu','kamis','jumat','sabtu','minggu']

now = 'senin'
x= int(hari.index(now))
brbhari= -1

future = brbhari % 7
a=future+x
print(hari[a])

# ========1 line============  
# print(hari[((brbhari%len(hari))+x)%7])