import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

TOKEN = ""

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

dp = Dispatcher()





btn1 = KeyboardButton(text="Шутер")
btn2 = KeyboardButton(text="Файтинг")
btn3 = KeyboardButton(text="Симулятор")
btn4 = KeyboardButton(text="Экшен")



janre_keyboard = ReplyKeyboardMarkup(
    keyboard=[[btn1], [btn2], [btn3], [btn4]],
    resize_keyboard=True
)



shooters = ['DOOM (2016): Скачать на Steam', 'Painkiller: Скачать на Steam', 'Quake Champions: Скачать на официальном сайте', 'BRAIN / OUT: Скачать на Steam', 'Strinova: Скачать на Steam']
fightings = ['Capcom Fighting Collection 2 Скачать на Steam', 'Fatal Fury: City of the Wolves Ссылка на официальную страницу игры', 'BLEACH: Rebirth of Souls Ссылка на страницу игры на сайте', 'Virtua Fighter 6 Ссылка на официальный сайт', 'Tekken 8 Скачать на Steam']
simulator = ['BeamNG.drive — Скачать на Steam', 'Manor Lords — Ссылка на Steam', 'InZOI — Ссылка на официальный сайт', 'PowerWash Simulator 2 — Скачать на Steam', 'Paralives — Ссылка на официальный сайт']
action = ['Kingdom Come: Deliverance II — Ссылка на официальный сайт', 'Assassins Creed: Shadows — Ссылка на официальный сайт', 'Grand Theft Auto VI — Ссылка на официальную страницу Rockstar Games', 'Split Fiction — Ссылка на официальную страницу игры', 'Ghost of Yotei — Ссылка на официальный сайт Sucker Punch']







@dp.message(Command("start"))
async def bot_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!"
                         f" Я помогу тебе выбрать игру! "
                         f"\n\nНапиши /help и я помогу тебе!")


@dp.message(Command("help"))
async def bot_help(message: Message):
    await message.answer("Все команды бота:\n/start - "
                         "старт бота\n/help - список команд\n"
                         "/games - стили игры")

@dp.message(Command("games"))
async def process_films_command(message: Message):
    await message.answer("Выберите стиль:", reply_markup=janre_keyboard)



@dp.message(F.text == "Шутер")
async def show_horror(message: Message):
    await message.answer("Держи шутер: " + random.choice(shooters))


@dp.message(F.text == "Файтинг")
async def show_action(message: Message):
    await message.answer("Держи файтинг игру: " + random.choice(fightings))

@dp.message(F.text == "Симулятор")
async def show_humor(message: Message):
    await message.answer("Держи симулятор игру: " + random.choice(simulator))

@dp.message(F.text == "Экшен")
async def show_fantasy(message: Message):
    await message.answer("Держи экшен игру: " + random.choice(actionp))

@dp.message()
async def unknown_message(message: Message):
    await message.answer("Я не понимаю тебя, напиши /help")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
