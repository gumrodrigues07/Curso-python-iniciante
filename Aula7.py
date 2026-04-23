lista_preco = [3500, 1000, 800, 3000]

#a1 = 0.2
#a2 = 0.10
#a3 = 0.05

def calcula_it(preco):
    if preco <= 2000:
        ir = 0.2 * preco
    else:
        ir = 0.3
    iss = 0.15 * preco
    csll = 0.05 * preco
    imposto_total = ir + iss + csll
    return imposto_total
        
for preco in lista_preco:
    imposto_total = calcula_it(preco)
    print(f"imposto total sobre o produto de R${preco}: {imposto_total}")

nova_lista_preco = [3000, 23990, 3212, 5109]

for preco in nova_lista_preco:
    imposto_total = calcula_it(preco)
    print(f"Imposto total sobre produto R${preco}: {imposto_total}")