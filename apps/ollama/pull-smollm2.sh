
./bin/ollama serve &

pid=$!

sleep 5


echo "Pulling smollm2:1.7b model"
ollama pull smollm2:1.7b


wait $pid
