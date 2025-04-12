lista = [10, 20, 30]

def show_index_value(lista):
  i = len(lista) - 1
  
  while i >= 0:
    print(f"índice {i} → valor {lista[i]}")
    i-=1
  
show_index_value([10, 20, 30])