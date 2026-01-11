# Image de base légère
FROM python:3.9-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Installation des dépendances
RUN pip install flask

# Copie du code
COPY app.py .

# Port exposé par le conteneur
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
