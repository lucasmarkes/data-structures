## O que é um array?

Um array é uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo. Os arrays são usados para armazenar dados em um formato organizado e acessível, permitindo que os programadores manipulem conjuntos de dados de maneira eficiente.
Os arrays são comumente usados em programação para armazenar listas de valores, como números, strings ou objetos. Eles podem ser unidimensionais (uma lista simples) ou multidimensionais (como matrizes), dependendo da necessidade do programador.

## Como criar um array
```python
# Criando um array unidimensional
array_unidimensional = [1, 2, 3, 4, 5]

# Criando um array multidimensional
array_multidimensional = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## Acessando elementos de um array
```python
# Acessando o primeiro elemento de um array unidimensional
primeiro_elemento = array_unidimensional[0]
print(primeiro_elemento)  # Saída: 1

# Acessando o segundo elemento de um array multidimensional
segundo_elemento = array_multidimensional[1][0]
print(segundo_elemento)  # Saída: 4
```

## Modificando elementos de um array
```python
# Modificando o primeiro elemento de um array unidimensional
array_unidimensional[0] = 10
print(array_unidimensional)  # Saída: [10, 2, 3, 4, 5]
# Modificando o segundo elemento de um array multidimensional
array_multidimensional[1][0] = 20
print(array_multidimensional)  # Saída: [[1, 2, 3], [20, 5, 6], [7, 8, 9]]
```

## Adicionando elementos a um array
```python
# Adicionando um elemento a um array unidimensional
array_unidimensional.append(6)
print(array_unidimensional)  # Saída: [10, 2, 3, 4, 5, 6]

# Adicionando um elemento a um array multidimensional
array_multidimensional[0].append(4)
print(array_multidimensional)  # Saída: [[1, 2, 3, 4], [20, 5, 6], [7, 8, 9]]
```

## Removendo elementos de um array
```python
# Removendo um elemento de um array unidimensional
array_unidimensional.remove(2)
print(array_unidimensional)  # Saída: [10, 3, 4, 5, 6]

# Removendo um elemento de um array multidimensional
array_multidimensional[1].remove(5)
print(array_multidimensional)  # Saída: [[1, 2, 3, 4], [20, 6], [7, 8, 9]]
```

## Iterando sobre um array
```python
# Iterando sobre um array unidimensional
for elemento in array_unidimensional:
    print(elemento)
# Saída: 10, 3, 4, 5, 6

# Iterando sobre um array multidimensional
for linha in array_multidimensional:
    for elemento in linha:
        print(elemento)
# Saída: 1, 2, 3, 4, 20, 6, 7, 8, 9
```