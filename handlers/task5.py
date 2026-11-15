import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message 

def start_funs(bot:Bot):
    @bot.on.message()
    async def name(message: Message):
        if message.text:
            text = message.text
        else:
            text = 'Текста нет'

        count = len(message.attachments)
        await message.answer(f'{count} вложений, {text}')


    





