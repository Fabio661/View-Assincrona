import asyncio
import httpx

async def contador_1():
    contador = 0
    while contador < 7:
        print(contador)
        contador = contador + 1
        await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)
 
async def espaco():
    contador = 0
    while contador < 7:
        print('-')
        contador = contador + 1
        await asyncio.sleep(1)
        
async def main():
    task = asyncio.create_task(contador_1())
    task2 = asyncio.create_task(espaco())
    
    await task
    await task2
    
asyncio.run(main())