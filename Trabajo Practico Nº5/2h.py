def mayorenLista(lista1):
    may=lista1[0]
    aux=lista1[0]
    for aux in lista1:
        if  aux>may:
            may=aux
    print(may)
mayorenLista( [2,3,4,5]) #5