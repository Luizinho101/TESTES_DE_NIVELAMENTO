# 📥 Projeto de Download e Compactação de Arquivos

Este projeto tem como objetivo baixar arquivos PDF de links públicos e compactá-los em um arquivo ZIP, organizando os arquivos dentro da estrutura de diretórios definida.

---

## 📁 Estrutura do Projeto

```bash
projeto/
│── src/
│   ├── baixar_arquivos.py
│   ├── zipar_arquivos.py
│   ├── downloads/
│── main.py
│── README.md


🚀 Como Executar

1️⃣ Clonar o Repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2️⃣ Instalar Dependências

pip install wget
3️⃣ Executar o Script Principal

python main.py
Isso irá:

Baixar os arquivos PDF para src/downloads/.

Criar um arquivo ZIP chamado arquivos_zipados.zip dentro de src/.

🔧 Funcionalidades
✔️ Download automático de arquivos PDF a partir de URLs públicas.
✔️ Organização dos arquivos dentro da pasta src/downloads/.
✔️ Compactação dos arquivos baixados em um arquivo ZIP.
✔️ Estrutura modular para facilitar a manutenção e reutilização do código.

📄 Licença
Este projeto é de código aberto e está sob a licença MIT.
Sinta-se livre para modificá-lo e distribuí-lo conforme necessário.
