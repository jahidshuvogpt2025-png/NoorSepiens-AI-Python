import re

from core.long_memory import add_memory



def extract_memory(text):

    text = text.strip()


    # Name memory

    match = re.search(
        r"আমার নাম\s+(.+)",
        text
    )

    if match:

        name = match.group(1).strip()

        add_memory(
            "identity",
            "name",
            name
        )



    # Call name

    match = re.search(
        r"আমাকে\s+(.+?)\s+বলে ডাকবে",
        text
    )

    if match:

        call_name = match.group(1).strip()

        add_memory(
            "identity",
            "call",
            call_name
        )



    # Age

    match = re.search(
        r"আমার বয়স\s+(.+)",
        text
    )

    if match:

        add_memory(
            "facts",
            "age",
            match.group(1).strip()
        )



    # Skill

    if "Python" in text or "পাইথন" in text:

        add_memory(
            "skills",
            "skill",
            "Python"
        )



    # Goal

    if "AI Engineer" in text or "এআই ইঞ্জিনিয়ার" in text:

        add_memory(
            "goals",
            "goal",
            "AI Engineer"
        )