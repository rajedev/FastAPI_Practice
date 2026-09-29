"""Native FastMCP server (no FastAPI): define tools with @mcp.tool and run with mcp.run()."""

from fastmcp import FastMCP

mcp = FastMCP(
    name="Standalone demo MCP",
    instructions="Example MCP server built only with FastMCP decorators.",
)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


@mcp.tool(name="greet")
def greet_user(name: str, excited: bool = False) -> str:
    """Say hello to someone."""
    msg = f"Hello, {name}"
    return f"{msg}!" if excited else msg


if __name__ == "__main__":
    mcp.run()
