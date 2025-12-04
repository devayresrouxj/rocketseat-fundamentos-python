print("For utilizando lista:")
lista = [1, 2, 3, 4, 5]

for elemento in lista:
  print(elemento)

print("For utilizando tupla:")
tupla = (1, 2, 3, 4, 5)

for elemento in tupla:
  print(elemento)

print("For utilizando dicionários:")
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("Chaves:")
for chave in pessoa.keys():
  print(chave)

print("Valores:")
for valor in pessoa.values():
  print(valor)

print("Chave e Valor:")
for chave, valor in pessoa.items():
  print(f"{chave} = {valor}")

# range() -> Retorna um intervalo numérico em formato de lista
for numero in range(5):
  print("Número:", numero)

# len() -> Retorna a quantidade de itens na lista
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
  print("Índice:", indice)
  print("Elemento:", lista[indice])

# enumerate() -> 
lista_enumarate = ['a', 'b', 'c']
for indice, valor in enumerate(lista_enumarate, start=1):
  print(f"{indice} - {valor}")