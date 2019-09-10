def menorenLista(lista1):
    min=lista1[0]
    aux=lista1[0]
    for aux in lista1:
        if  aux<min:
            min=aux
    print(min)
menorenLista( [2,3,4,5]) #2