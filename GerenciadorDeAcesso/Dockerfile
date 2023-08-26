# Image
FROM python:3.11.4-slim

# setando o diretório de trabalho no container
WORKDIR /app

# Copiando dependencias no container
COPY requirements.txt .

# Instalando dependencias no container
RUN pip install --no-cache-dir -r requirements.txt

# Copiando arquivos do projeto para o container
COPY . .

# Comandos para rodar a aplicação
RUN python migracao.py

CMD ["python", "Menu.py"]



