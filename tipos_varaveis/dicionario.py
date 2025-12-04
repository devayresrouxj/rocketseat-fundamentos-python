# Declaração
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("Meu dicionário de exemplo:", pessoa)

# Acessando propriedades
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Criando nova propriedade
pessoa["sobrenome"] = "Silva"
print("Meu dicionário modificado:", pessoa)

# Métodos
# del -> Remove um par chave e valor
del pessoa["sobrenome"]
print("Dicionário após o del:", pessoa)

# keys() -> Retorna todas as chaves do dicionário
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# values() -> Retorna todos os valores de um dicionário
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor:", valores[0])

# items() -> Retorna uma lista de tuplas contendo chaves e valor
itens = list(pessoa.items())
print("Chave e valor do dicionário:", itens)
print("Primeiro par de chave e valor:", itens[0])
print("Chave do primeiro par:", itens[0][0])
print("Valor do primeiro par:", itens[0][1])