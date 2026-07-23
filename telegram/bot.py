import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

from user.profile import create_user
from core.agent import NoorAgent



agent = NoorAgent()



async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    create_user(
        user.id,
        user.username or "",
        user.first_name or ""
    )


    await update.message.reply_text(
        "🤖 NoorSepiens AI Python Version চালু হয়েছে ✅"
    )





async def chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text


    reply = agent.response(text)


    await update.message.reply_text(
        reply
    )






def run_bot():


    app = Application.builder().token(
        os.getenv("BOT_TOKEN")
    ).build()



    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat
        )
    )


    print(
        "NoorSepiens Python Bot Started 🚀"
    )


    app.run_polling()
