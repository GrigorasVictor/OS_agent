import os

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from src.prompts import *

MCP_HOST = os.getenv('MCP_HOST', '127.0.0.1')
MCP_PORT = os.getenv('MCP_PORT', '8010')
MODEL_NAME = os.getenv('MODEL_NAME', 'qwen3-vl:4b')
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://127.0.0.1:11434')

MCP_SERVER_URL = f"http://{MCP_HOST}:{MCP_PORT}/mcp"


root_agent = LlmAgent(
    model=LiteLlm(model=f'ollama_chat/{MODEL_NAME}'),
    name="system_administration",
    description=(
        description
    ),
    instruction=instruction,
    tools=[
        McpToolset(
           connection_params=StreamableHTTPConnectionParams(
               url=MCP_SERVER_URL,
           ),
       )
    ],
)
