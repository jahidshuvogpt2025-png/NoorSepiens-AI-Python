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

from core.memory_extractor import extract_memory



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

Memory Engine v2 চালু হয়েছে ✅

আমি আপনার তথ্য মনে রাখতে পারবো।

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

    try:


        text = update.message.text



        # Extract user information
        extract_memory(
            text
        )



        # AI response
        reply = agent.response(
            text
        )



        await update.message.reply_text(
            reply
        )



    except Exception as error:


        print(
            "CHAT ERROR:",
            error
        )


        await update.message.reply_text(
            "AI error হয়েছে ❌"
        )









# ================= RUN BOT =================


def run_bot():


    token = os.getenv(
        "BOT_TOKEN"
    )



    if not token:

        print(
            "BOT_TOKEN missing ❌"
        )

        return




    app = Application.builder().token(
        token
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
        "NoorSepiens AI Memory Engine v2 Started 🚀"
    )



    app.run_polling()