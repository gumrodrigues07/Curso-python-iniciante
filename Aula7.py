lista_preco = [1500, 1000, 800, 3000]

#a1 = 0.2
#a2 = 0.10
#a3 = 0.05

for preco in lista_preco:
    ir = 0.2 * preco
    iss = 0.15 * preco
    csll = 0.05 * preco
    imposto_total = ir + iss + csll
    print(f"imposto total sobre o produto de R${preco}: {imposto_total}")