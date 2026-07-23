import sys
import os

# project root path add
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from telegram.bot import run_bot



def main():

    print("Starting NoorSepiens AI Python 🚀")

    run_bot()



if __name__ == "__main__":

    main()
