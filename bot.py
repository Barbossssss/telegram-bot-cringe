import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

seen_users = set()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in seen_users:
        await message.answer(
            "👋 Привет!\n\n"
            "Отправляя любые материалы через этого бота (включая фото и текст),\n"
            "вы подтверждаете, что:\n"
            "• Имеете согласие от изображённых лиц;\n"
            "• Несёте полную ответственность за загружаемый контент;\n"
            "• Понимаете, что материалы могут быть опубликованы на канале.\n\n"
            "Продолжая пользоваться ботом, вы автоматически соглашаетесь с этими условиями."
        )
        seen_users.add(user_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
