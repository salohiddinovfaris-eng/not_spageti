import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message

async def start_func(bot:Bot):

    @bot.on.message(text=['помощь', 'о боте'])
    async def func2(message:Message):
        await message.answer('Ну их очень много мне лень их перечислять')