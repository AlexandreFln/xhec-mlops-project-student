# Make sure to check bin/run_services.sh, which can be used here

# Do not forget to expose the right ports! (Check the PR_4.md)

# Utiliser une image de base avec Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /xhec-mlops-project-student

# Copier les fichiers de l'application
COPY . .

# Rendre le script exécutable
RUN chmod +x ./bin/run_services.sh
RUN pip install pip-tools
# Install dependencies
RUN pip-compile requirements.in
RUN pip-compile requirements-dev.in
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
RUN pip install pre-commit
RUN pre-commit run --all-files --show-diff-on-failure

EXPOSE 8001
EXPOSE 4002
# Health check to ensure the application is running
HEALTHCHECK CMD curl --fail http://localhost:4201/_stcore/health || exit 1 && curl --fail http://localhost:8001/_stcore/health || exit 1
ENTRYPOINT ["./bin/run_services.sh"]