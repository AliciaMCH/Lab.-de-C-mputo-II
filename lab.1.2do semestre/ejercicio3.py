#MACHUCA CHAMORRO ALICIA
a= []

for i in range(6):
     a.append([])
     for j in range(6):
             a[i].append(i+j)
d=[]
matriz=([[fila[i]for fila in a]for i in [0,1,2,3,4,5]])
d.append(matriz)

f=[]
for i in d:
	for w in i:
		f.append(w)
		for y in f:
			suma=0
			suma=sum(y)
		print(suma)
