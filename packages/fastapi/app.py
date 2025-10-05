import requests

from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/ask')
def ask(prompt :str):
    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        "stream" : False,
        "model" : "smollm2:1.7b"
    })

    return Response(content=res.text, media_type="application/json")

@app.get('/embedding')
def embedding(prompt :str):
    res = requests.post('http://ollama:11434/api/embeddings', json={
        "prompt": prompt,
        "stream" : False,
        "model" : "smollm2:1.7b"
    })

    return Response(content=res.text, media_type="application/json")