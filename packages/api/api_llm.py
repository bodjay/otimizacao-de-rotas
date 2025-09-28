from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoint para processar resultados e gerar relatórios
@app.route('/processar_resultados', methods=['POST'])
def processar_resultados():
    dados = request.json
    if not dados or 'solucao' not in dados:
        return jsonify({'erro': 'Dados inválidos'}), 400

    solucao = dados['solucao']

    # Simulação de integração com LLM (exemplo com Ollama)
    resposta_llm = consultar_llm(solucao)

    return jsonify({'relatorio': resposta_llm})

def consultar_llm(solucao):
    """
    Consulta a LLM para gerar um relatório baseado na solução fornecida.
    """
    # Exemplo de chamada para uma API de LLM
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma3:1b",
        "prompt": f"Gere um relatório detalhado para a solução: {solucao}"
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get('text', 'Erro ao gerar relatório')
    else:
        return f"Erro na consulta à LLM: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)