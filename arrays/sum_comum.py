def soma_unicos(lista):
  contados = [] 
  total = 0
  for i in lista:
    if i not in contados:
      count = 0

      for j in lista:
        if j == i:
          count += 1

      contados.append(i)
      
      if count == 1:
        total = total + i
    
  print(total)
  
soma_unicos([1, 2, 3, 2, 4, 1]) 