FROM python:3.11-slim

# Installer les bibliothèques système nécessaires
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Créer le dossier de travail
WORKDIR /app

# Copier les dépendances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script
COPY test1.py /app/

# Lancer le script automatiquement
CMD ["python", "test1.py"]
