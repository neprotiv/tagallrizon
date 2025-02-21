import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

TOKEN = "8096351638:AAEGObv0GyM_pnZ_-OlI5ijOOREEezYEeS0"  # Вставьте сюда ваш токен
bot = Bot(token=TOKEN, default=types.DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

@dp.message(Command("all"))
async def tag_all(message: Message):
    chat_id = message.chat.id
    members = []
    async for member in bot.get_chat_members(chat_id):  # Получаем список всех участников
        if not member.user.is_bot:
            members.append(f"<a href='tg://user?id={member.user.id}'>{member.user.first_name}</a>")
    
    if members:
        mention_text = ", ".join(members)
        await message.reply(f"@all {mention_text}")
    else:
        await message.reply("Не удалось получить список участников.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
