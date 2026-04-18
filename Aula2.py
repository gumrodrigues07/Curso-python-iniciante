faturamento = 2300
custo = 38
lucro = faturamento/custo
margem_lucro = lucro/faturamento
email_cliente = "nofanafarofa@gmail.com"

#maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)
#minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# @
print(email_cliente.find("@")) # -1 quando nao encontrar

# tamanho do texto
print(len(email_cliente))

# pegar um caracter
print(email_cliente[5])

#pegar um trecho do texto
print(email_cliente[:12])

#trocar um trecho do texto
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

nome = "gustavo rodrigues"
# trabalhar com nomes
print(nome.capitalize())
print(nome.title())

email_cliente = "gimrodrigues07@gmail.com"
#pegar servidor do email
posicao_arroba = email_cliente.find("@")+1
servidor = email_cliente[posicao_arroba:]
print("servidor: ", servidor)
#pegar o nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
print(primeiro_nome.capitalize())
#pegar o segundo nome
segundo_nome = nome[posicao_espaco+1:]
print(segundo_nome.capitalize())

# casos especiais
margem_lucro = round(margem_lucro, 2)
print(f"economia da empresa: R${faturamento:.2f}, R${custo:.2f}, R${lucro:.2f}, {margem_lucro:.0%}")

