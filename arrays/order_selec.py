def ord_sel(lista):
  novo_array = []

  for i in range(len(lista)):
    # Busca o menor elemento (mesmo que a função buscaMenor)
    menor = lista[0]
    menor_indice = 0

    for j in range(1, len(lista)):
      if lista[j] < menor:
        menor = lista[j]
        menor_indice = j

    print(f"Iteração {i+1}: menor = {menor}, índice = {menor_indice}")
    print(f"Lista antes: {lista}")
    print(f"Removendo {lista[menor_indice]}")
    
    novo_array.append(lista.pop(menor_indice))

    print(f"Lista depois: {lista}")
    print(f"Novo array: {novo_array}\n")

  return novo_array

# Executa a ordenação com passos visíveis
ord_sel([5, 3, 6, 2, 11, 10])
