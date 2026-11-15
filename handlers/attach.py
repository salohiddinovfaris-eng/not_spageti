import sys 
from pathlib import Path
import random

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message 
from vkbottle import PhotoMessageUploader # Модуль для того чтобы бот отправлять фото а не ссылки на фото

def start_func(bot: Bot):

    @bot.on.message()
    async def attach_hendler(message: Message):
        attachments = message.attachments
        user_id = message.from_id
        for i in attachments:
            if i.type == 'photo':
                photo = i.photo
                photo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfYtPtI-RlSWwcwu6QqgFlQiLjq25VryqdbMLz_7QX-Q&s=10'
                await message.answer('Вы отправили фото')
                # await message.answer('Вы отправили фото', attachment = photo_url)
                # await message.answer(f'ID фото {photo.id}')
                # await message.answer(f'ID владельца фото {photo.owner_id}, {user_id}')
                # await message.answer(f'Размеры фото {photo.sizes}')

            if i.type == 'sticker':
                await message.answer('Вы отправили стикер')

            if i.type == 'doc':
                await message.answer('Вы отрпавили документ')