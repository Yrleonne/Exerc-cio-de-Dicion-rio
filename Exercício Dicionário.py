# 1 - Crie um dicionário simples
#aluno = {
 #   'nome': 'Yrleonne Albuquerque',
 #   'idade': 36,
 #   'nota':7.5
}
#print(aluno)

# 2 - Acessando valores
#produto = {'nome': 'caneta', 'preço': 2.5, 'estoque': 100}
#print('produto:', produto['nome'])
#print('quantidade em estoque', produto['estoque'])

# 3 - Adicionando novos pares chave-valor
#pessoa = {'nome': 'carlos', 'idade': 30}
#pessoa['cidade'] = 'são paulo'
#print(pessoa)

# 4 - Removendo elementos
#carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
#carro.pop('ano')
#print(carro)

# 5 - Verificando existência de uma chave
#contato = {"nome": "Ana", "email": "ana@email.com"}
#if "telefone" in contato:
#    print("A chave 'telefone' existe no dicionário.")
#else:
#    print("A chave 'telefone' NÃO existe no dicionário.")

# 6 - Contando frequência de palavras
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
def contar_palavras(lista):
    contagem = {}
    for palavra in lista:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
resultado = contar_palavras(palavras)

print(resultado)

# 7 - Invertendo um dicionário
d = {"a": 1, "b": 2, "c": 3}
d_invertido = {valor: chave for chave, valor in d.items()}
print(d_invertido)

# 8 -  