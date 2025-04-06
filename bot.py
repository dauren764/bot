import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Пример словаря
words = [
    {"word": "challenge", "translation": "вызов", "example": "Learning English is a challenge."},
    {"word": "success", "translation": "успех", "example": "Success comes from hard work."},
    {"word": "freedom", "translation": "свобода", "example": "Everyone deserves freedom."},
    {"word": "journey", "translation": "путешествие", "example": "Life is a journey."},
    {"word": "future", "translation": "будущее", "example": "The future is in your hands."},

    {"word": "hope", "translation": "надежда", "example": "Never lose hope."},
    {"word": "create", "translation": "создавать", "example": "We can create our own future."},
    {"word": "goal", "translation": "цель", "example": "My goal is to learn English."},
    {"word": "strong", "translation": "сильный", "example": "You are stronger than you think."},
    {"word": "learn", "translation": "учиться", "example": "I want to learn new things every day."},

    {"word": "focus", "translation": "сосредоточиться", "example": "Focus on your goals."},
    {"word": "dream", "translation": "мечта", "example": "Never stop chasing your dream."},
    {"word": "smart", "translation": "умный", "example": "She is very smart and talented."},
    {"word": "believe", "translation": "верить", "example": "Believe in yourself."},
    {"word": "change", "translation": "изменение", "example": "Change starts from within."},

    {"word": "kind", "translation": "добрый", "example": "Its important to be kind to others."},
    {"word": "brave", "translation": "смелый", "example": "Be brave and take the risk."},
    {"word": "happy", "translation": "счастливый", "example": "Do what makes you happy."},
    {"word": "honest", "translation": "честный", "example": "He is always honest with his friends."},
    {"word": "energy", "translation": "энергия", "example": "She has a lot of positive energy."},

    {"word": "respect", "translation": "уважение", "example": "Respect is earned, not given."},
    {"word": "growth", "translation": "рост", "example": "Personal growth takes time."},
    {"word": "trust", "translation": "доверие", "example": "Trust is the foundation of any relationship."},
    {"word": "peace", "translation": "мир", "example": "We all want to live in peace."},
    {"word": "patience", "translation": "терпение", "example": "Patience is key to success."},
]

# Словарь для избранных слов
favorites = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для изучения английских слов.\nКоманды:\n/word — новое слово\n/quiz — мини-тест\n/save — сохранить слово\n/favorites — избранные слова")

async def word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word_data = random.choice(words)
    context.user_data["current_word"] = word_data
    await update.message.reply_text(
        f"Word: {word_data['word']}\nTranslation: {word_data['translation']}\nExample: {word_data['example']}"
    )

async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    word = context.user_data.get("current_word")
    if word:
        favorites.setdefault(user_id, []).append(word)
        await update.message.reply_text(f"Слово '{word['word']}' сохранено в избранное.")
    else:
        await update.message.reply_text("Сначала получи слово с помощью /word.")

async def favorites_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    fav = favorites.get(user_id, [])
    if fav:
        text = "\n".join([f"{w['word']} – {w['translation']}" for w in fav])
        await update.message.reply_text("Твои избранные слова:\n" + text)
    else:
        await update.message.reply_text("У тебя пока нет избранных слов.")

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word_data = random.choice(words)
    context.user_data["quiz_word"] = word_data
    options = [word_data["translation"]]
    while len(options) < 4:
        option = random.choice(words)["translation"]
        if option not in options:
            options.append(option)
    random.shuffle(options)
    keyboard = [[opt] for opt in options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text(f"Что означает слово: {word_data['word']}?", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quiz_word = context.user_data.get("quiz_word")
    if quiz_word:
        answer = update.message.text
        if answer == quiz_word["translation"]:
            await update.message.reply_text("Правильно!")
        else:
            await update.message.reply_text(f"Неправильно. Правильный ответ: {quiz_word['translation']}")
        context.user_data["quiz_word"] = None

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token("7755761485:AAEQ_j1CqXhZH-la2Q1267SMIZfSridMFg0").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("word", word))
    app.add_handler(CommandHandler("save", save))
    app.add_handler(CommandHandler("favorites", favorites_list))
    app.add_handler(CommandHandler("quiz", quiz))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен!")
    app.run_polling()