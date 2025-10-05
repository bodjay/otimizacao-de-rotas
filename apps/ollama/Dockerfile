# Dockerfile de Produção para o Ollama
FROM ollama/ollama:stable

COPY ./pull-smollm2.sh /pull-smollm2.sh

RUN chmod +x /pull-smollm2.sh

CMD ["/bin/sh", "/pull-smollm2.sh"]