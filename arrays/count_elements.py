def contar_frequencia(lista):
  contados = [] 

  for i in lista:
    if i not in contados:
      count = 0

      for j in lista:
        if j == i:
          count += 1

      contados.append(i)
      
      if count > 1:
        print(f"{i} aparece {count} vezes")
  
contar_frequencia([1, 2, 2, 3, 3, 3, 4])