# image
FROM python:3.10.12-slim

# répertoire de travail
WORKDIR /app

# fichiers de dépendances
COPY requirements.txt .

# installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# copier le reste du code
COPY . .

# port
EXPOSE 8080

# lancer le serveur FastAPI avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
