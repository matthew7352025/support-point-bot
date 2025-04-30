
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте. Я бот 'Точка Опоры'. Вы можете рассказать мне, что чувствуете — я рядом и готов помочь."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()
    response = "Спасибо, что поделились. Я рядом."

    if "тревога" in user_text or "боюсь" in user_text:
        response = "Понимаю. Давайте вместе попробуем немного расслабиться. Сделайте глубокий вдох... и медленный выдох. Вы не один."
    elif "один" in user_text or "одиночество" in user_text:
        response = "Чувство одиночества бывает тяжёлым. Но уже тот факт, что вы обратились ко мне — это шаг к теплу и заботе."
    elif "плохо" in user_text or "тяжело" in user_text:
        response = "Жаль, что вам сейчас тяжело. Иногда просто выговориться — уже облегчение. Расскажите, что случилось."

    await update.message.reply_text(response)

app = ApplicationBuilder().token("YOUR_TOKEN_HERE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
