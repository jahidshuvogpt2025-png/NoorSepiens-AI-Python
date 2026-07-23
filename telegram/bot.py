import os

from dotenv import load_dotenv

from telegram import Update

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)


from user.profile import create_user

from user.profile_card import generate_profile

from core.agent import NoorAgent



load_dotenv()



agent = NoorAgent()





# ================= START =================


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

        """
🤖 NoorSepiens AI

Python Version চালু হয়েছে ✅

আমি আপনার কথা মনে রাখতে পারবো।

প্রশ্ন করুন।
"""

    )






# ================= PROFILE =================


async def profile(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    card = generate_profile()



    await update.message.reply_text(

        card

    )







# ================= CHAT =================


async def chat(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    text = update.message.text



    reply = agent.response(

        text

    )



    await update.message.reply_text(

        reply

    )









# ================= BOT RUN =================


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

        CommandHandler(

            "profile",

            profile

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
