''' 
Asynchronous programming in Python allows you to write code that can handle multiple tasks concurrently, making it possible to perform I/O-bound tasks like web requests, file I/O, and database operations more efficiently. 
This is achieved using asyncio, a module introduced in Python 3.4, which provides the foundation for writing asynchronous code.

Key Concepts
Event Loop: The core of asynchronous programming in Python. It runs asynchronous tasks and callbacks, handles I/O operations, and runs until complete.
Coroutines: Special functions defined with async def that can be paused and resumed, making them suitable for non-blocking operations.
Tasks: Wrappers around coroutines that run concurrently.
Futures: Represent the result of an asynchronous operation.

'''

# Creating a Coroutine

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Running the coroutine
asyncio.run(greet())

# Running Multiple Coroutines Concurrently

async def greet2(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}")

async def main():
    task1 = asyncio.create_task(greet2("Alice", 1))
    task2 = asyncio.create_task(greet2("Bob", 2))
    
    await task1
    await task2

asyncio.run(main())

# asyncio.gather can be used to run multiple coroutines concurrently and wait for all of them to finish.

async def main2():
    await asyncio.gather(
        greet2("Alice", 1),
        greet2("Bob", 2),
        greet2("Charlie", 1)
    )

asyncio.run(main2())


# Making Asynchronous HTTP Requests

import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'https://www.example.com',
        'https://www.python.org',
        'https://www.github.com'
    ]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
