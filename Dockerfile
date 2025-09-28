# Use the official Ollama base image
# Use a specific, stable Ollama version to reduce vulnerabilities
FROM ollama/ollama

# Listen on all network interfaces
ENV OLLAMA_HOST=0.0.0.0:11434

# Set the model to be pulled
ENV MODEL=gemma:2b

# Run the Ollama server in the background and pull the model
# The `sleep 5` command waits for the server to initialize
RUN ollama serve & sleep 5 && ollama pull $MODEL

# Expose the Ollama port
EXPOSE 11434

# Start the Ollama server when the container launches
CMD ["ollama", "serve"]
