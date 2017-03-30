#MACHUCA CHAMORRO ALICIA
M= [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
x=0
for i in  range(0,4):
    for y in  range (0,4):
        suma=0
        for j in  range(y,y+3):
            suma= suma + M[i][j] + M[i+2][j]
        suma = suma+ M[i+1][y+1]
        if x<suma:
            x=suma
        suma=0

print x
