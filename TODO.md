# TODO

0. Diagrama de arquitetura da solução

1. Sistema de Otimização de Rotas via Algoritmos Genéticos
Página 5 de 8
    ● Desenvolver um sistema que resolva o problema do caixeiro viajante
        (TSP) para otimizar rotas de entrega de medicamentos e insumos:
        ○ Implementar a representação genética adequada para rotas;
        ○ Desenvolver operadores genéticos especializados (seleção, crossover, mutação) para o problema de roteamento;
        ○ Criar uma função fitness que considere distância, prioridade de entregas e outras restrições relevantes.
    ● Incluir restrições realistas como:
            ○ Prioridades diferentes para entregas (medicamentos críticos vs. insumos regulares);
            ○ Capacidade limitada de carga dos veículos;
            ○ Autonomia limitada dos veículos (distância máxima que pode ser percorrida);
            ○ Múltiplos veículos disponíveis (ampliando para o problema de roteamento de veículos - VRP);
            ○ Outras restrições que achar interessante.
        ** Agregar restrições nas etapas: **
                ○ Fitness
                ○ Mutação
    ● Visualizar as rotas otimizadas em um mapa para fácil interpretação.

4. Integração com LLMs para Geração de Instruções e Relatórios
    ● Utilizar uma LLM pré-treinada para:
        ○ Gerar instruções detalhadas para motoristas e equipes de entrega com base nas rotas otimizadas;
        ○ Criar relatórios diários/semanais sobre eficiência de rotas, economia de tempo e recursos;
        ○ Sugerir melhorias no processo com base nos padrões identificados.

    ● Implementar prompts eficientes para extrair informações úteis da LLM;
    ● Permitir que o sistema responda as perguntas em linguagem natural sobre as rotas e entregas.
        ○ Criar API que consulte e processe os resultados da solução 
        ○ Criar interface de comunicação com a LLM
            ○ Ollama com smoll2:1.7T



5. Código e Organização (para ambos os projetos)
    ● Projeto Python bem estruturado, utilizando ambiente virtual (Poetry,
    Pipenv ou venv);
    ● Documentação detalhada, incluindo diagramas de arquitetura;
    ● Testes automatizados para validação de funcionalidades;
    ● Se optou pela implementação em nuvem: infraestrutura como código
    (IaC) para provisionamento dos recursos