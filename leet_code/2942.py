
def findWordsContaining(words: list[str], x: str) -> list[int]:
  lista = []
  for i in range(len(words)):
    if x in words[i]:
      lista.append(i)
      
  return lista

print(findWordsContaining(words=["pay","attention","practice","attend"], x="at"))