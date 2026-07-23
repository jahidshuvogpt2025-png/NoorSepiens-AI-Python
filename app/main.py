import sys
import os


# Add project root path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from telegram_bot.bot import run_bot




def main():

    print(
        "Starting NoorSepiens AI Python 🚀"
    )


    run_bot()




if __name__ == "__main__":

    main()
