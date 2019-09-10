def mayorenLista(lista1):
    may=lista1[0]
    min=lista1[0]
    aux=lista1[0]
    for aux in lista1:
        if  aux>may:
            may=aux
        if  aux<min:
            min=aux
    print(may)
    print(min)
mayorenLista( [2,3,4,5]) #5