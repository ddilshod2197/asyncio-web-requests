import aiohttp
import asyncio

async def sozlash():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
            return await response.json()

async def main():
    posts = await sozlash()
    for post in posts:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://jsonplaceholder.typicode.com/posts/{post["id"]}') as response:
                print(await response.json())

asyncio.run(main())
```

```python
import aiohttp
import asyncio

async def sozlash(session):
    async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        posts = await sozlash(session)
        tasks = []
        for post in posts:
            task = asyncio.create_task(sozlash(session))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

asyncio.run(main())
```

```python
import aiohttp
import asyncio

async def sozlash(session, id):
    async with session.get(f'https://jsonplaceholder.typicode.com/posts/{id}') as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        posts = await sozlash(session, 1)
        tasks = []
        for post in posts:
            task = asyncio.create_task(sozlash(session, post["id"]))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

asyncio.run(main())
