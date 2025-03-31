import wget
import os


def baixar_arquivos():
    """
    Faz o download dos arquivos necessários.
    """
    link_anexo1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    link_anexo2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

    arquivos = [
        ("ANEXO_I.pdf", link_anexo1),
        ("ANEXO_II.pdf", link_anexo2)
    ]

    for arquivo, link in arquivos:
        if not os.path.exists(arquivo):
            print(f"Baixando {arquivo}...")
            wget.download(link, arquivo)
            print(f"\nDownload concluído: {arquivo}")
        else:
            print(f"{arquivo} já existe. Pulando download.")
