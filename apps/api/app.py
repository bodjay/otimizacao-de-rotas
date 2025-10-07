import json
import ollama
from src.tools import calculate_route_by_restrictions  as crr

from fastapi import FastAPI, Response

app = FastAPI()

model = "smollm2:1.7b"

@app.get('/ask')
def ask(prompt :str):
    try:
        with open('data/municipios.json', 'r') as file:
            municipios = json.load(file)

            # Example of using a custom tool to calculate a route with restrictions
            # using X and Y coordinates
            # tool = crr.calculate_route_by_restrictions([(123, 456), (789, 101), (901, 123), (345, 678)], ["no highways", "avoid tolls"])
            res = ollama.chat(model=model,messages=[{"role": "user", "content": prompt}], tools=[
                # tool
                ])
  
            output = ollama.generate(
                model=model,
                system="You are a helpful assistant that uses tools to answer questions. Use {municipios} to find information about Brazilian municipalities.",
                temperature=0.1,
                prompt=f"Using this data: {res.message.content}. Respond to this prompt: {prompt}"
            )

            return Response(content=output.response, media_type="application/json")
    except FileNotFoundError:
        print("Error: 'data.json' not found.")
        return Response(content={"error": "'data.json' not found."}, media_type="application/json")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'data.json'.")
        return Response(content={"error": "Invalid JSON format"}, media_type="application/json")

@app.get('/embedding')
def embedding(prompt :str):
    res = ollama.embed(model=model, input=prompt)
    return Response(content=res.embeddings, media_type="application/json")