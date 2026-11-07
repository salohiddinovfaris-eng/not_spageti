import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message 

async def start_funs(bot:Bot):

    @bot.on.message(text='имя')
    async def func3(message:Message):
        user_id = message.from_id
        user = await message.ctx_api.users.get(user_ids=user_id)
        first_name = user[0].first_name
        await message.answer(f'Твое имя: {first_name}')