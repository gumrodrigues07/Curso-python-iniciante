faturamento = 1000 # tipo int -> numero inteiro
bonus = 3.4 # tipo float -> numero casa decimal
custo = 27.47
imposto = faturamento*0.73
total = faturamento*bonus-custo-imposto
lucro = faturamento-custo-imposto
Margem_Lucro = lucro / faturamento
Mensagem = "o caralho da conta da"
vendas_novas = 400
faturamento = faturamento+vendas_novas
print("oraoraoraoraoraora")
print("Aninha Meu Amor TOOOOOOOSO")
print("o faturamento foi de", faturamento)
print("o lucro foi de ", lucro)
print("a margem de lucro foi de", Margem_Lucro)
print("o total foi de", round(total, 1))
contrato_anos = 137 / 12
contrato_meses = 137 % 12
print("tempo de contrato", int(contrato_anos), "anos e", contrato_meses, "meses")