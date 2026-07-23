import re

from core.long_memory import add_memory




def convert_bangla_number(text):

    bangla = "০১২৩৪৫৬৭৮৯"
    english = "0123456789"

    result = ""

    for ch in text:

        if ch in bangla:

            result += english[
                bangla.index(ch)
            ]

        else:

            result += ch


    return result






def extract_memory(text):


    memories = []



    # Name

    name = re.search(
        r"আমার নাম\s+([^\s,.!?]+)",
        text
    )


    if name:

        add_memory(
            "identity",
            "name",
            name.group(1)
        )

        memories.append(
            "name"
        )





    # Call preference

    call = re.search(
        r"আমাকে\s+(.+?)\s+বলে ডাকবে",
        text
    )


    if call:

        add_memory(
            "identity",
            "call",
            call.group(1)
        )

        memories.append(
            "call"
        )







    # Age

    age = re.search(
        r"আমার বয়স\s*([০-৯0-9]+)",
        text
    )


    if age:

        add_memory(
            "facts",
            "age",
            convert_bangla_number(
                age.group(1)
            )
        )

        memories.append(
            "age"
        )







    # Skill

    skill = re.search(
        r"(Python|JavaScript|AI|প্রোগ্রামিং)",
        text,
        re.IGNORECASE
    )


    if skill:

        add_memory(
            "skills",
            "skill",
            skill.group(1)
        )

        memories.append(
            "skill"
        )






    # Goal

    if "AI Engineer" in text or "এআই ইঞ্জিনিয়ার" in text:


        add_memory(
            "goals",
            "goal",
            "AI Engineer"
        )


        memories.append(
            "goal"
        )





    return memories
