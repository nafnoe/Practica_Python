v= [12,7,25,4,18,9]
print("Vector sin ordenar: ", v)
def procedimiento_Ordenar(v):
    i = 0
    j = 0
    aux = 0
    for i in range (0,5):
        for j in range ((i+1), 6):
            if v[i] > v[j]:
                aux = v [i]
                v[i] = v[j]
                v[j] = aux

procedimiento_Ordenar(v)
print("Vector ordenado: ",v)
