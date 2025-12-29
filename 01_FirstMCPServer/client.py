import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

async def main():
    url = "http://127.0.0.1:8000/mcp"
    async with streamable_http_client(url) as (read, write, get_session_id):
        async with ClientSession(read, write) as session:
            print("Before Initialize: Session ID =", get_session_id())
            
            await session.initialize()
            
            sid = get_session_id()
            print("After Initialize: Session ID =", sid)
            
            result = await session.call_tool("add", {"a": 5, "b": 7})
            print("Result of add(5, 7):", result)
            
if __name__ == "__main__":
    asyncio.run(main())



