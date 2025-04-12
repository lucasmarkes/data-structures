def intersecao(lista1, lista2):
  retorno = []
  
  for item in lista1:
    if item in lista2 and item not in retorno:
      retorno.append(item)
  return retorno

print(intersecao([1, 2, 3], [2, 3, 4]))
