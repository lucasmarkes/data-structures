def encontrar_dois_maiores(lista):
    if lista[0] > lista[1]:
        max1 = lista[0]
        max2 = lista[1]
    else:
        max1 = lista[1]
        max2 = lista[0]

    for i in lista[2:]:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i

    print('Maior:', max1)
    print('Segundo maior:', max2)
    
encontrar_dois_maiores([10, 20, 30, 15, 24])
