# janela selecionar pasta do pc
import os
import shutil
from tkinter.filedialog import askdirectory

nome_pasta_sel = askdirectory()
print(nome_pasta_sel)

lista_arquivos = os.listdir(nome_pasta_sel)
print(lista_arquivos)

#fazer o backup dos arquivos que estão nessa pasta
nome_p_backup = "backup"
nome_comp_backup = f"{nome_pasta_sel}/{nome_p_backup}"
if not os.path.exists(nome_comp_backup):
        os.mkdir(nome_comp_backup)

for arquivo in lista_arquivos:
    print(arquivo)
    nome_comp = f"{nome_pasta_sel}/{arquivo}"
    nome_final = f"{nome_comp_backup}/{arquivo}"
    if "." in arquivo:
        shutil.copy2(nome_comp, nome_final)
    elif "backup" != arquivo:
        shutil.copytree(nome_comp, nome_final)