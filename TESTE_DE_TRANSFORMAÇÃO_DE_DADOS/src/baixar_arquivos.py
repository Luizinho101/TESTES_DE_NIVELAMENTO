import wget
import os


def baixar_arquivos():
    pasta_destino = "src/downloads"
    os.makedirs(pasta_destino, exist_ok=True)

    linkAnexo1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    linkAnexo2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

    caminho1 = os.path.join(pasta_destino, "ANEXO_I.pdf")
    caminho2 = os.path.join(pasta_destino, "ANEXO_II.pdf")

    wget.download(linkAnexo1, caminho1)
    wget.download(linkAnexo2, caminho2)

    print("\nArquivos baixados com sucesso!")


if __name__ == "__main__":
    baixar_arquivos()
