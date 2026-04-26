# Bibliotecas que vou utilizar
import os
import shutil
import datetime
from tkinter.filedialog import askdirectory

# Selecionar pasta
nome_pasta = askdirectory() #Pede para selecionar a pasta para definir variável
lista_arquivos = os.listdir(nome_pasta)#listdir() lista os arquivos do diretório

# Criar pasta "backup" para 1º backup e definir data para para backups posteriores
data_hoje = datetime.datetime.today().strftime("%Y.%m.%d %H.%M.%S")
pasta_b = "backup"
nome_comp_b = f"{nome_pasta}/{pasta_b}"

if not os.path.exists(nome_comp_b):
    os.mkdir(nome_comp_b)

# Definir nome completo e nome final dos arquivos
for arquivo in lista_arquivos:
    nome_comp = f"{nome_pasta}/{arquivo}"
    nome_final = f"{nome_comp_b}/{data_hoje}/{arquivo}"

# Criar pastas de backups posteriores ao primeiro
    if not os.path.exists(f"{nome_comp_b}/{data_hoje}"):
        os.mkdir(f"{nome_comp_b}/{data_hoje}")

# Fazer backup
    if "." in arquivo:
        shutil.copy2(nome_comp, nome_final)
    elif "backup" != arquivo:
        shutil.copytree(nome_comp, nome_final)