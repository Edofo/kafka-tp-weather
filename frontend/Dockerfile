# Utiliser l'image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer Streamlit et les autres dépendances
RUN pip3 install --no-cache-dir streamlit
RUN pip3 install kafka-python
# Copier les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Définir la commande à exécuter lorsque le conteneur démarre
CMD ["streamlit", "run", "index.py", "--server.port=8501", "--server.address=0.0.0.0"]
