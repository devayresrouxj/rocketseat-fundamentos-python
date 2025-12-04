nome = "Gabriel"
sobrenome = "Casemiro"
nome_completo = "Gabriel Casemiro"

# upper() -> Deixa tudo em maiúsculo
print(nome.upper())

# lower() -> Deixa tudo em minúsculo
print(nome.lower())

# Exibindo uma posição de caracter específico []
print(nome[1])

# count() -> Conta a quantidade de ocorrências de um caracter
print(nome_completo.count("a"))

# find() -> Retorna o índice de um caracter
print(nome_completo.find("e"))

# encode() -> Converte a string para bytes
print(nome_completo.encode())

# decode() -> Converte bytes para string
print(nome_completo.encode().decode())

# replace() -> Substitui uma ocorrência por outra
print(nome_completo.replace("a", "123"))

# join() -> Adiciona um separador a cada caracter
print("-".join(nome))

# split() -> Converte string em lista
print(nome_completo.split(" "))

# strip() -> Remove subjacente de um caracter alvo
print("xGabriel Casemirox".strip("x"))

# rstrip() -> Remove caracter alvo a direita
print("xGabriel Casemirox".rstrip("x"))

# lstrip() -> Remove caracter alvo a esquerda
print("xGabriel Casemirox".lstrip("x"))

# startswith() -> Se uma string começa com determinado caracter
print(nome_completo.startswith("G")) 

# endswith() -> Se uma string termina com determinado caracter
print(nome_completo.endswith("G")) 

# in -> Verifica se existe uma string 
print("el" in nome_completo)

# not in -> Verifica se não existe uma ocorrência em uma string
print("el" not in nome_completo)