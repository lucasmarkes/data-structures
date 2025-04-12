def remover_duplicados(lista):
  new_list = []
  
  for i in lista:
    if i not in new_list:
      new_list.append(i)
  
  return(new_list)

print(remover_duplicados([1, 2, 2, 3, 1, 4]))