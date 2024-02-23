import aiohttp
import asyncio
from django.http import JsonResponse

urls = ["https://quotable.io/quotes?page=1", 'https://randomuser.me/api/']

async def combined(request):
    async def get(session, url):
        async with session.get(url) as response:
            return await response.json()
        
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get(session, url))) 
        
        response = await asyncio.gather(*tasks)
    return JsonResponse({"Response": response},safe=False)