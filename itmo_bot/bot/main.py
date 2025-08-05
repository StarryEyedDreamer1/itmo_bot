
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from bot.handlers import start, help_command, compare, recommend_start, recommend_input, cancel
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('recommend', recommend_start)],
        states={1: [MessageHandler(filters.TEXT & ~filters.COMMAND, recommend_input)]},
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("compare", compare))
    app.add_handler(conv_handler)

    print("Бот запущен")
    app.run_polling()

if __name__ == '__main__':
    run_bot()
