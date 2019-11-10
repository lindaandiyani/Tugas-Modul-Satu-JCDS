nama = 'purwAdhika startup dan coding schOol'
print(nama.count('s'))


# ======= WITHOUT COUNT===============
# CARA PERTAMA
nama= ' Hari ini hari tidak masuk sekolah'
cari = 'H'
x = nama.upper().replace(cari.upper(),'')
jumlahcari= len(nama)-len(x)

print('jumlah huruf a adalah',jumlahcari)

# CARA KEDUA
kalimat= 'Hari ini Hari tidak masuk sekolah'
found = 'hari'
y=kalimat.lower().replace(found.lower(),'')
jmlfound= (len(kalimat) - len(y)) // len(found)

print(jmlfound)
