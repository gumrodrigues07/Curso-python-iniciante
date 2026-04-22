dic_produtos = {"iphone": 6000, "airpod": 550, "ipad": 9000, "macbook": 11000}

#pegar elemento
print(dic_produtos["iphone"])

#editar elemento
dic_produtos["iphone"] = dic_produtos["iphone"] *1.32
print(dic_produtos["iphone"])

#quantidade itens
print(len(dic_produtos))

#remover item do dicionario
print(dic_produtos.pop("iphone"))

#adicionar item ao dicionário
dic_produtos["iphone"]=6300
print(dic_produtos)

#verificar se item existe no dicionário
if "iphone" in dic_produtos:
    print("produto existe")
else:
    print("não existe isso")

#verificar se um valor existe nos valores do dicionário
#if 6300 in dic_produtos.values():
#    print("existe")
#else:
#    print("não existe tbm")

nome_produto = input("nome do produto: ").lower()
preco_produto = float(input(f"preço do produto: "))
dic_produtos[nome_produto] = preco_produto
#cadastrar novo produto
#caso exista, editar
print(dic_produtos)

#além disso programa tem que atualizar o preço de todos os produtos
#os novos valores que são 10% a mais
#dic_produtos.values = dic_produtos.values *1.10


for produto in dic_produtos:
    novo_preco = dic_produtos[produto] *1.1
    dic_produtos[produto] = novo_preco
    print(dic_produtos)