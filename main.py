import asyncio
import os 
from dotenv import load_dotenv
import ssl
import aiohttp

from vkbottle import Bot, API, AiohttpClient
from handlers import start, echo, task1, task2, task3, task4


from vkbottle_types.responses.messages import MessagesSendPeerIdsResponse
from vkbottle_types.objects import MessagesSendUserIdsResponseItem

MessagesSendPeerIdsResponse.model_rebuild(
    force=True,
    _types_namespace={
        "MessagesSendUserIdsResponseItem": MessagesSendUserIdsResponseItem
    }
)

async def main():
    load_dotenv()

    token = os.getenv('VK_TOKEN')

    if not token:
        raise RuntimeError("Переменна VK_TOKEN не задана")

    ssl_context = ssl.create_default_context()

    http_client = AiohttpClient(connector=aiohttp.TCPConnector(ssl=ssl_context))

    api = API(token=token, http_client=http_client)
    print("Генератор токена:", type(api.token_generator).__name__)
    bot = Bot(api=api)


    # await start.start_func(bot)
    # await echo.start_func(bot)
    # await task1.start_func(bot)
    # await task2.start_func(bot)
    # await task3.start_funs(bot)
    await task4.start_funс(bot)

    await bot.run_polling()

if __name__ == '__main__':
    asyncio.run(main())