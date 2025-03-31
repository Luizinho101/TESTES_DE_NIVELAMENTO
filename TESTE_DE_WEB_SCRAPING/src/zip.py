import zipfile
import os


def zipar_arquivos(arquivos, nome_zip):
    """
    Zipa uma lista de arquivos em um arquivo ZIP.

    Args:
        arquivos (list): Lista de arquivos a serem zipados.
        nome_zip (str): Nome do arquivo ZIP a ser criado.
    """
    arquivos_existentes = [
        arquivo for arquivo in arquivos if os.path.exists(arquivo)]

    if not arquivos_existentes:
        print("Erro: Nenhum arquivo encontrado para zipar.")
        return

    with zipfile.ZipFile(nome_zip, 'w') as arquivo_zip:
        for arquivo in arquivos_existentes:
            arquivo_zip.write(arquivo)
            print(f"Adicionado ao ZIP: {arquivo}")

    print(f"Arquivos zipados com sucesso em '{nome_zip}'")
