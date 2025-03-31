import zipfile
import os


def zipar_arquivos():
    pasta_destino = "src/downloads"
    nome_do_arquivo_zip = "src/Teste_LuizAntonio.zip"

    arquivos_para_zipar = [
        os.path.join(pasta_destino, "ANEXO_I.pdf"),
        os.path.join(pasta_destino, "ANEXO_II.pdf")
    ]

    with zipfile.ZipFile(nome_do_arquivo_zip, 'w') as arquivo_zip:
        for arquivo in arquivos_para_zipar:
            arquivo_zip.write(arquivo, os.path.basename(arquivo))

    print(f"Arquivos zipados com sucesso em '{nome_do_arquivo_zip}'")


if __name__ == "__main__":
    zipar_arquivos()
