import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message

async def Echo_bot(bot:Bot):
  
    @bot.on.message()
    async def Echo(message:Message):
        text = message.text.lower()
        spl = text.split(' ')
        value = False

        for word in spl:
            word = word.strip(". , ; : ? ! ... — - « » “ ” ( ) [ ] { } § № * & @ # % ‰ / \ | ₽ $ € £ ¥ '")
            if word == 'пароль' or word == 'секрет':
                value = True
            else:
                pass

        if value:
            await message.answer("Я никому не скажу! 🤫")
        else:
            await message.answer(message.text)