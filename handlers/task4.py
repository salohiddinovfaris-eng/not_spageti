import sys 
from pathlib import Path
import random

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message 

choises = ['орел', 'решка']

async def start_funс(bot:Bot):
    states = {}
    
    @bot.on.message(text=['start', 'начать', 'привет'])
    async def func4(message:Message):

        user_id = message.from_id
        user = await message.ctx_api.users.get(user_ids=user_id)
        first_name = user[0].first_name

        await message.answer(f'Привет {first_name}')
        await message.answer('Сыграем в Орел и Решка? Если хочешь напиши: "играть"')

    @bot.on.message(text=['Играть', 'играть'])
    async def Orel_i_Reshka(message:Message):

        await message.answer('Выбирай Орел или Решка')

        @bot.on.message(text=['Орел', 'орел', 'Решка', 'решка'])
        async def Orel_i_Resha_answer(message:Message):

            text = message.text.lower()
            choise = random.choice(choises)

            if text == choise:
                await message.answer('Ты победил')

            else: 
                await message.answer('Повезет в следуйщий раз')