S = {0,1,2,3,4,5,6,7,8,9,10}
A = {3,5,7}
B = {5,7,9} 

print ('irisan dari A dan B :',A.intersection(B))
print ('gabungan dari A dan B :', A.union(B))
print(' A irisan  A gabungan B ', A.intersection(A.union(B)))
print('B irisan  A gabungan B',B.intersection(A.union(B)))
print ((A.union(B).intersection(A.union(B))))
print ((A.intersection(B)).union(A.union(B)))