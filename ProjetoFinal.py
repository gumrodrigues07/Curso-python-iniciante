# janela selecionar pasta do pc
import os
import shutil
import datetime
from tkinter.filedialog import askdirectory

nome_pasta_sel = askdirectory()

lista_arquivos = os.listdir(nome_pasta_sel)

#fazer o backup dos arquivos que estão nessa pasta
data_hoje= datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")
nome_p_backup = "backup"
nome_comp_backup = f"{nome_pasta_sel}/{nome_p_backup}"
if not os.path.exists(nome_comp_backup):
        os.mkdir(nome_comp_backup)

for arquivo in lista_arquivos:
    nome_comp = f"{nome_pasta_sel}/{arquivo}"
    nome_final = f"{nome_comp_backup}/{data_hoje}/{arquivo}"

    if not os.path.exists(f"{nome_comp_backup}/{data_hoje}"):
        os.mkdir(f"{nome_comp_backup}/{data_hoje}")

    if "." in arquivo:
        shutil.copy2(nome_comp, nome_final)
    elif "backup" != arquivo:
        shutil.copytree(nome_comp, nome_final)