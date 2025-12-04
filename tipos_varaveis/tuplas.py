# Declaração
minha_tupla = (1, 2, 2, 3, 4)
print("Minha tupla:", minha_tupla)

# Exibindo elementos
print("minha_tupla[0]:", minha_tupla[0])
print("minha_tupla[2]:", minha_tupla[2])

# Exibindo o último elemento
print("minha_tupla[-1]", minha_tupla[-1])

# count() -> Retorna a quantidade de vezes que um elemento aparece
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

# index() -> Retorna o índice de um elemento
indice = minha_tupla.index(3)
print("Posição do elemento 3:", indice)