import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
import requests
logging.basicConfig(level=logging.INFO) 

TOKEN = ""
API_KEY = ""

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher() 

@dp.message(Command("start"))
async def bot_start(message: Message): 
    await message.answer(f"Привет, {message.from_user.full_name}!"
                         f" Я помогу тебе узнать погоду! "
                         f"\n\nНапиши /help и я помогу тебе!")

@dp.message(Command("help"))
async def bot_help(message: Message):
    await message.answer("Все команды бота:\n/start - "
                         "старт бота\n/help - список команд\n"
                         "/weather - погода")

@dp.message(Command("weather"))
async def cmd_weather(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Пожайлуйста, укажите город после команды /weather!")
        return

@dp.message(Command("test"))
async def cd_test(message: types.Message):
    await message.answer(text="Hello <i>World</i>", parse_mode=ParseMode.HTML)

# Команда 'mark' с использованием MarkdownV2
@dp.message(Command("mark"))
async def cd_test2(message: types.Message):
    text = (
        "*Жирный текст*\n"
        "_Курсив_\n"
        "~Зачеркнутый~\n"
        "`Моноширинный текст`\n"
        "```Python\nprint('Hello, world!')\n```\n"
        "[Ссылка](https://example.com)"
    )
    await message.answer(text, parse_mode=ParseMode.MARKDOWN_V2)



    city = args[1]
    try:
        req = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params={'q': city, 'appid': API_KEY, 'units': 'metric', 'lang': 'ru'})

        req.raise_for_status()
        data = req.json()

        if 'main' in data:
            temp = data['main']['temp']
            feels = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            await message.answer(
                f"🌍 Погода в городе <b>{city}</b>:\n"
                f"🌤 Температура: <b>{temp}°C</b>\n"
                f"🌡 По ощущениям: <b>{feels}°C</b>\n"
                f"💦 Влажность: <b>{humidity}%</b>\n"
                f"💨 Ветер: <b>{wind} м/с</b>"
            )
        else:
            await message.answer("Город не найден, попробуйте ещё раз.")

    except requests.exceptions.RequestException:
        await message.answer("Ошибка при получении данных о погоде. Попробуйте позже.")

@dp.message()
async def echo_message(message: Message):
    await message.answer("Я не понимаю тебя, напиши /help")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
            
