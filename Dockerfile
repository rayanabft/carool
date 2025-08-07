FROM python:3.11-slim

# Installer libGL pour OpenCV
RUN apt-get update && apt-get install -y libgl1 && apt-get clean

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script principal
COPY test1.py /app/

# Lancer le script Python
CMD ["python", "test1.py"]