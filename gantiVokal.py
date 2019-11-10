def vokal (kalimat):
    kalimat= kalimat.lower().replace('a','o')
    kalimat= kalimat.lower().replace('i','o')
    kalimat= kalimat.lower().replace('u','o')
    kalimat= kalimat.lower().replace('e','o')
    print(kalimat)
vokal('nama')

# def ubahVokal(kata):
#     output=''
#     for huruf in kata:
#         if huruf in 'aiueo':
#             output=output+'o'
#         else:
#             output=output+huruf
#     return(output)
# print(ubahVokal('nama'))