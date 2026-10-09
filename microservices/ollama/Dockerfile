FROM ollama/ollama:latest

# Accept build argument from docker-compose
ARG MODEL
ENV MODEL=${MODEL}



RUN ollama serve & SERVER_PID=$! && \
        sleep 5 && \
        ollama pull ${MODEL} && \
        kill $SERVER_PID

CMD ["serve"]

