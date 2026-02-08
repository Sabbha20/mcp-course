import asyncio
from fastmcp import Client

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        if client.is_connected:
            print("Connected with FastMCP server.")
            
        tools = await client.list_tools()
        print(f"---- Available Tools: ----\n{tools}")
        
        response = await client.call_tool("add", {"a": 5, "b": 7})
        print(f"Result: {response}")
                    
if __name__ == "__main__":
    asyncio.run(main())



