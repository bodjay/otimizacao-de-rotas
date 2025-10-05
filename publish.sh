#!/bin/bash

# Script para construir e publicar imagens Docker para produção

# Nome do repositório Docker Hub
REPO="seu-usuario/otimizacao-de-rotas"

# Construir e publicar cada serviço
docker build -f packages/frontend/Dockerfile.prod -t $REPO-frontend:latest ./packages/frontend
docker push $REPO-frontend:latest

docker build -f packages/otimizador/Dockerfile.prod -t $REPO-otimizador:latest ./packages/otimizador
docker push $REPO-otimizador:latest

docker build -f packages/fastapi/Dockerfile.prod -t $REPO-api:latest ./packages/fastapi
docker push $REPO-api:latest

docker build -f packages/ollama/Dockerfile.prod -t $REPO-ollama:latest ./packages/ollama
docker push $REPO-ollama:latest

echo "Imagens publicadas com sucesso!"