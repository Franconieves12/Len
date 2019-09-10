def promLista(lista1):
    acum=0
    cant_num=len(lista1)
    for sum in lista1:
        acum+=sum
    print(acum/cant_num)
promLista( [2,3,4,5]) # 3.5
