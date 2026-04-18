#for
lista_vendas = [1000, 2000, 15300, 11032, 5000]
meta = 1100
Percentual_bonus = 0.2
venda = 1000

#for i in range(10): executa o código o numero de vezes que pedir
#    print("oraoraoraoraoraoraoraoraoraora")
#print("oraoraoraoraoraorao")

for venda in lista_vendas:
    if venda >= meta:
        bonus = venda * Percentual_bonus
        print("meta alcançada")
        print(f"Bonus recebido = {bonus}")
    else:
        bonus = 0
        print("meta não atingida")
        print(f"bonus recebido = {bonus}")

#for venda in lista_vendas:
#   print(venda)
#    print("Próxima venda")
    #tudo o que for ser executado várias vezes, é escrito dentro
