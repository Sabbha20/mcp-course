from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo-server")

@mcp.tool(description="Add 2 numbers")
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")