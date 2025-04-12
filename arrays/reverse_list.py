def inverter_lista(lista):
  new_list = []
    
  for i in lista:
      new_list.insert(0, i)
  
  return new_list

print(inverter_lista([1, 2, 3]))