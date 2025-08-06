FROM python:3.11-slim

# Créer le dossier de travail
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script Python
COPY test1.py /app/

# Exposer le port si nécessaire (ex: 8000)
# EXPOSE 8000

# Commande de démarrage
CMD ["python", "test1.py"]
