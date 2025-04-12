# Dada uma lista de números, ordene manualmente (sem usar sort() nem sorted()) em ordem crescente.

# entrada - lista = [4, 1, 3, 9, 2]
# saida - [1, 2, 3, 4, 9]

def sortarray(lista):
  for i in range(len(lista)): # percorre a lista
    for j in range(len(lista) - 1): # comparar os elementos
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  return(lista)

print(sortarray([4, 1, 3, 9, 2]))