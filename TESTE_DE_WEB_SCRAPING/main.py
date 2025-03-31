from src.download import baixar_arquivos
from src.zip import zipar_arquivos


def main():
    baixar_arquivos()

    arquivos_para_zipar = ["ANEXO_I.pdf", "ANEXO_II.pdf"]
    nome_do_arquivo_zip = "Teste_LuizAntonio.zip"

    zipar_arquivos(arquivos_para_zipar, nome_do_arquivo_zip)


if __name__ == "__main__":
    main()
