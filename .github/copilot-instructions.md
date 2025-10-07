# Instruções para Agentes de IA no Projeto de Otimização de Rotas

## Visão Geral do Projeto
Este repositório implementa um sistema de otimização de rotas para distribuição de medicamentos e insumos hospitalares. Ele utiliza algoritmos genéticos para resolver problemas de roteamento (como o problema do caixeiro viajante e VRP) e integra modelos de linguagem (LLMs) para geração de relatórios e instruções.

### Principais Componentes
1. **FastAPI Service** (`packages/fastapi`):
   - Fornece uma API para interagir com modelos de linguagem (LLMs).
   - Endpoints principais:
     - `/ask`: Gera respostas baseadas em prompts.
     - `/embedding`: Retorna embeddings para prompts fornecidos.
   - Integração com o serviço `ollama` para comunicação com modelos LLM.

2. **Otimização de Rotas** (`packages/otimizador`):
   - Implementa algoritmos genéticos para otimização de rotas.
   - Arquivos principais:
     - `genetic_algorithm.py`: Contém funções para geração de populações, cálculo de fitness, cruzamento e mutação.
     - `tsp.py`: Integra o algoritmo genético com visualizações usando Pygame.
   - Suporte para benchmarks como `att48` e problemas customizados.

3. **Frontend** (`packages/frontend`):
   - (Ainda em desenvolvimento) Provavelmente será usado para visualização e interação com o sistema.

4. **Ollama Service** (`packages/ollama`):
   - Scripts e configurações para gerenciar modelos de linguagem.

## Fluxos de Trabalho Críticos

### Instalação
1. Instale as dependências do otimizador:
   ```bash
   pip install -r packages/otimizador/requirements.txt
   ```
2. Para o FastAPI:
   ```bash
   pip install -r packages/fastapi/requirements.txt
   ```

### Execução do Serviço FastAPI
1. Navegue até o diretório `packages/fastapi`.
2. Execute o servidor:
   ```bash
   uvicorn app:app --reload
   ```

### Testando o Algoritmo Genético
1. Execute o script `tsp.py` para visualizar a otimização de rotas:
   ```bash
   python packages/otimizador/tsp.py
   ```

### Uso de Docker
- Cada componente possui um `Dockerfile` ou `Dockerfile.prod` para facilitar a execução em contêineres.
- Exemplos:
  - Build e execução do FastAPI:
    ```bash
    docker build -t fastapi-service -f packages/fastapi/Dockerfile .
    docker run -p 8000:8000 fastapi-service
    ```

## Convenções e Padrões
- **Algoritmos Genéticos**:
  - A população inicial pode ser gerada de forma aleatória ou heurística.
  - Métodos de seleção incluem roleta, torneio e elitismo.
  - O cruzamento utiliza a técnica de "Order Crossover (OX)".

- **Visualização**:
  - O Pygame é usado para desenhar cidades, rotas e gráficos de desempenho.

- **Integração com LLMs**:
  - O serviço FastAPI se comunica com o `ollama` para geração de respostas e embeddings.

## Dependências Externas
- **Python**:
  - Bibliotecas principais: `pygame`, `numpy`, `requests`, `fastapi`, `uvicorn`.
- **Docker**:
  - Usado para empacotamento e execução de serviços.

## Arquivos Importantes
- `README.md`: Documentação geral do projeto.
- `src/otimizador/genetic_algorithm.py`: Implementação do algoritmo genético.
- `apps/api/app.py`: API para interação com LLMs.
- `docker-compose.yml`: Configuração para orquestração de contêineres (se aplicável).

---

Sinta-se à vontade para ajustar ou expandir estas instruções conforme necessário para refletir mudanças no projeto.