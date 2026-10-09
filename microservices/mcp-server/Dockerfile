FROM python:3.12-slim

WORKDIR /app

# Copy server code and requirements for MCP server
COPY server/server.py /app/
COPY server/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Default envs (can be overridden by docker-compose)
ENV MCP_NAME=system_admin_mcp \
    MCP_HOST=0.0.0.0 \
    MCP_PORT=8000 \
    MCP_TRANSPORT=streamable-http

EXPOSE 8000

CMD ["python", "server.py"]
