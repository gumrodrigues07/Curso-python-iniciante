#if condicao/comparacao:
    # tudo o que for pra fazer se a condicao verdadeira
#else:
    #tudo o que acontece se a condicao for falsa

#primeiro cenário
nome = input("Primeiro e último nome: ").title()
if nome.find(" ") == -1:
    print("Erro")
else:
    vendas = float(input("suas vendas: "))
    meta = 5800
    manda_toma_no_cu = "vai tomar no cu,"
    chama_de_pobre = "pobre"
    posicao_espaco = nome.find(" ")
    Primeiro_nome = nome[:posicao_espaco]
    segundo_nome = nome[posicao_espaco+1:]

    #comparadores

    # > maior que
    # < menor que
    # >= maior ou igual que
    # <= menor ou igual que
    # == igual
    # != diferente

    #if vendas >= meta:
    #    print("Vendedor ganha bonus")
    #    print("Vendedor bateu a meta")
    #    bonus = 0.3*vendas
    #    
    #    print("Bonus do vendedor: ", bonus)
    #else:
    #    print(manda_toma_no_cu, chama_de_pobre)
    #    print("Não bate meta não come, vaza daqui")
    #print("falou")

    # Segundo cenário
    mínimo = 4900
    meta_1 = meta
    meta_2 = 7200
    meta_3 = 10000

    if vendas >= meta_3:
        print(f"Meu amigo {Primeiro_nome}, satisfacão pra caralho")
        print("Bateu todas as metas")
        bonus = 0.5*vendas
        bonus = f"{bonus:.2f}"
        print("Seu bonus foi de: ",bonus)
    else:
        if vendas >= meta_2:
            print("O cara é foda, patroa")
            print("Bateu duas metas")
            bonus = 0.3*vendas
            bonus = f"{bonus:.2f}"
            print("Seu bonus foi de:",bonus)
        else:
            if vendas >= meta_1:
                print("porrrra, tudo isso?")
                print("Bateu a primeira meta")
                bonus = 0.1*vendas
                bonus = f"{bonus:.2f}"
                print("Seu bonus foi de: ",bonus)
            else:
                if vendas >= mínimo:
                    print("Ainda bem")
                    print("Manteve o emprego")
                    print("Fique esperto, ninguém é insubstituível")
                else:
                    print("Seu desempenho não atende ao esperado")
                    print("Aguarde o movimento de seus superiores")
print("Então vou indo")