"""
Author: Rajendhiran Easu
Date: 28/04/26
Description:
"""

from fastmcp import FastMCP
from fastmcp.server.providers.openapi import RouteMap, MCPType

from app.practice.main import app

mcp = FastMCP.from_fastapi(app=app,
                           route_maps=[  # Force all GET requests to be Tools instead of Resources
                               RouteMap(methods=["GET"], mcp_type=MCPType.TOOL)])

if __name__ == "__main__":
    mcp.run()