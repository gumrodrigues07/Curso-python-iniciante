# inputs
#email = input("E-mail: ")
#nome = input("Primeiro e ultimo nome: ").title()
#espaço_nome = nome.find(" ")
#primeiro_nome = nome[:espaço_nome]
#segundo_nome = nome[espaço_nome+1:]
#print(f"{primeiro_nome}, por favor, verifique o e-mail {email}")

# listas
vendas = [100, 200, 20, 35]

#soma de elementos
vendas_total = sum(vendas)
print(vendas_total)

#Tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

#Máximo e mínimo
print(max(vendas))
print(min(vendas))

#Pegar elemento
print(f"{vendas[1]}, {vendas[3]}")

lista_produtos = ["iphone", "xiaomi", "poco", "fones"]
#produto_procurado = input("Pesquise: ").lower()
#print(produto_procurado in lista_produtos)

#add item na lista
lista_produtos.append("relógios")
print(lista_produtos)

#remover item da lista
lista_produtos.remove("iphone")
print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)

#editar item
preço = [672, 52, 340]
print(preço)
preço[0] = 673
print(preço)
preço[2] = preço[2] *1.03
print(preço)

#contar quantas vezes item aparece
poco = ["poco c85", "poco c75", "poco x7 pro", "poco c85", "poco c85", "poco x7 pro"]
print(poco.count("poco c85"))

#ordenar lista
lista_produtos.sort()
preço.sort(reverse=True)
print(lista_produtos)
print(preço)