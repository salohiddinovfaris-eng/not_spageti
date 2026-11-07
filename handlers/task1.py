import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message

async def start_func(bot:Bot):

    @bot.on.message(text=['start', 'привет'])
    async def func1(message:Message):
        await message.answer('Привет! Я учебный VK-бот')