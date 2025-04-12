def find_min_max(lista):
  min = lista[0]
  max = lista[0]
  
  for i in lista:
    if i < min:
      min = i
    if i > max:
      max = i
      
  print(min,max)    
    
find_min_max([5, 9, 2, 14, 7])