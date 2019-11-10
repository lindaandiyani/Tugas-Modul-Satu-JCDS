jumlahhewan= 13
jumlahkaki=32
kakiayam=2
kakikambing=4


selisihkaki= abs(kakikambing-kakiayam)
nAyam= abs(jumlahkaki-(kakiayam)*jumlahhewan)/selisihkaki

print(nAyam)


# ================SOAL KEDUA===================
# pers 1       andiskrg = jumlahusia-ayahskrg

# pers 2       ayahskrg-masalalu = rasio(jumlahusia-ayahskrg-masalalu)
'''
STEP
            ayahskrg = (rasio(jumlahusia-ayahskrg-masalalu)) + masalalu
            ayahskrh=(rasio*jumlahusia-rasio*ayahskrg -rasio*masalalu) +masalalu
            ayahskrg +rasio*ayahskrg = (rasio*jumlahusia)-rasio*masalalu + masalalu
            ayahskrg(1+rasio) = rasio*jumlahusia-rasio*masalalu + masalalu
            ayahskrg =((rasio*jumlahusia)-(rasio*masalalu) + masalalu)/(1+rasio)      
'''
jumlahusia = 50
rasio = 6
masalalu= 4

ayahskrg = (rasio*jumlahusia-rasio*masalalu + masalalu)/(1+rasio)
print(ayahskrg)

# =========SOAL KETIGA==========
'''
pers 1.     umurAsekrg-selisihmasalalu = (rasiodulu*(umuribu-selisihmasalalu))-selisihdulu

pers 2.     umurAskrg = rasioskrg*umuribu + selisihumurskrg
STEP
((rasioskrg*umuribu)+selisihumurskrg) -selisihmasalalu= (rasiodulu*(umuribu-selisihmasalalu)-selisihumurdulu)
rasioskrg*umuribu = ((rasiodulu*(umuribu-selisihmasalalu))-selisih umur dulu-selisihumurskrg+selisihmasalalu
rasioskrg * umuribu = (rasiodulu*umuribu-rasiodulu*selisihmasalalau)-selisihumurdulu-selisihumuskrg +selisihmasalalu
rasioskrg*umuribu - umuribu*rasiodulu =-rasiodulu*selisihmasalalau)-selisihumurdulu-selisihumuskrg +selisihmasalalu
umuribu (rasioskrg-rasiodulu) = -rasiodulu*selisihmasalalau)-selisihumurdulu-selisihumuskrg +selisihmasalalu
uumuribu = (-rasiodulu*selisihmasalalu-selisihumurdulu-selisihumurskrg +selisihmasalalu)/(rasioskrg-rasiodulu)


umuriskrg = ((1/4*(umuribuskrg-selisih))-1/2)*7
'''
rasioskrg = 1/7
rasiodulu= 1/4
selisihmasalalu =19
selisihumurdulu = 1/2
selisihumurskrg = 19
 
umuribuskrg = ((-rasiodulu*selisihmasalalu)-selisihumurdulu-selisihumurskrg +selisihmasalalu)/(rasioskrg-rasiodulu)
print(umuribuskrg)



