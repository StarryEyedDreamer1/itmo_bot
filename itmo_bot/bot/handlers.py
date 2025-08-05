
from telegram import Update
from telegram.ext import ContextTypes
from bot.recommender import recommend_disciplines

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помогу тебе выбрать между программами магистратуры ИИ.\n"
        "Доступные команды:\n"
        "/compare — сравнить программы\n"
        "/recommend — получить рекомендации\n"
        "/help — помощь"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я умею:\n"
        "/compare — показать разницу между программами\n"
        "/recommend — подобрать предметы по твоему бэкграунду\n"
        "/cancel — завершить диалог"
    )

async def compare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Программа «ИИ» — больше математики и R&D.\n"
        "Программа «ИИ в продуктовой разработке» — упор на управление ИТ-продуктами и прикладные навыки.\n"
        "Обе длятся 2 года, очно. Выбор зависит от твоих целей."
    )

async def recommend_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Расскажи о своём бэкграунде и целях — например, 'Я программист, хочу работать в ML'")
    return 1

async def recommend_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    recommendation = recommend_disciplines(user_input)
    await update.message.reply_text(recommendation)
    return -1

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Диалог завершён.")
    return -1
