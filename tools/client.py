from fastmcp import Client
import asyncio

if __name__ == "__main__":
    client = Client("http://localhost:8000/mcp")

    async def main():        
        async with client:      
            tools = await client.list_tools()
            print("Ferramentas disponíveis no MCP:", tools)      
            print("\nTestando:")
            
            coordinates_response: dict = await client.call_tool("city_coords", {"city": [
                "São Paulo",
                "Rio de Janeiro",
                "Belo Horizonte",
                "Brasilia",
                "Curitiba",
                "Porto Alegre"
            ]})

            response: dict = await client.call_tool("tsp_solver", {
                "cities": coordinates_response.data,
                "priorities": [1, 1, 0, 1, 0, 0],
                "vehicle_capacity": 100,
                "max_distance": 1000,
            })

            print("Melhor rota encontrada:", [item['nome'] for item in response.data])

    asyncio.run(main())