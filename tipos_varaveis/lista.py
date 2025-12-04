# Declaração
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

print("Minha lista de exemplo: ", minha_lista)

# Exibindo elementos da lista
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])

# Selecionando o intervalo de uma lista (fatiamento)
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[3:]:", minha_lista[3:])

# Mudando um valor na lista
minha_lista[0] = "Python"
print("Minha lista de exemplo:", minha_lista)

# Métodos de lista
# append() -> Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# index() -> Retorna o índice do elemento
indice =  minha_lista.index(6)
print("Índice do elemento 6:", indice)

# insert() -> Adiciona um elemento a um índice específico
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# pop() -> Remove e retorna o elemento de um índice específico
elemento_removido = minha_lista.pop(0)
print("Elemento removido:", elemento_removido)
print("Após o pop(0):", minha_lista)

# remove() -> Remove o primeiro elemento com o valor específicado
minha_lista.remove(True)
print("Após o remove(True):", minha_lista)

# sort() -> Organiza a lista em ordem crescente
lista_numeros = [5, 7, 2, 1, 10, 55]
lista_numeros.sort()
print("Após sort():", lista_numeros)