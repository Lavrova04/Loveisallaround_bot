# app/main.py
import logging
from aiogram import Bot, Dispatcher, executor, types
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден. Добавь его в .env")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = (
        "👋 Привет! Добро пожаловать в *SoulMatch* 💘\n\n"
        "Этот бот создан для знакомств без границ — любовь, дружба и общение 🌍.\n\n"
        "👉 Начни прямо сейчас: заполни анкету и ищи свои первые мэтчи!\n\n"
        "🔗 Username бота: @loveisallaround_bot"
    )
    await message.answer(text, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
