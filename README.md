# OS Agent - SysAI System Administrator Assistant

This project was developed as part of the Operating Systems Administration (ASO) course. It features an intelligent system administrator assistant built using the Google ADK (Agent Development Kit) and the Model Context Protocol (MCP).

## Features

- SysAI Agent: An AI agent capable of providing system information and executing administration tasks.
- MCP Tools:
    - get_device_hardware_info: Details about CPU, RAM, and Disk.
    - list_process: Lists active processes ordered by resource consumption.
    - list_directory / get_file_content: Navigation and file reading (with security restrictions).
    - verify_flag: A specific tool for verifying the content of a protected file (flag.txt).
- Docker Infrastructure: Standardized deployment using Docker Compose.
- Ollama Integration: Support for local Large Language Models (LLMs).

## Project Structure

- src/: Source code for the ADK agent (agent.py) and prompts (prompts.py).
- server/: Implementation of the MCP server using FastMCP.
- microservices/: Dockerfiles for Ollama, MCP Server, and ADK Agent.
- docs/: Additional documentation and reference files.

## Requirements

- Docker and Docker Compose
- NVIDIA GPU (optional, for hardware acceleration)
- Git

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/GrigorasVictor/OS_agent.git
   cd OS_agent
   ```

2. Launch services:
   ```bash
   docker-compose up --build
   ```
   This starts:
   - Ollama: LLM engine (port 11434).
   - MCP Server: Tool server (port 8010).
   - ADK Web: Agent web interface (port 8000).

3. Access the Agent:
   Open a web browser at http://localhost:8000.

## Security and File Access

The agent is restricted to access files within the Windows path C:\Users\Victor\Documents, which is mapped to /host-project in the container. Direct access to sensitive files like flag.txt is blocked via server-side validations.

## Development Notes

For local execution in an IDE:
- Configure a Python interpreter with dependencies from requirements.txt.
- Run the command "adk web" or configure a corresponding Run Configuration.
- Ensure environment variables MCP_HOST, MCP_PORT, and OLLAMA_BASE_URL are correctly set.
