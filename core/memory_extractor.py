import re

from core.memory_engine import memory




def extract_memory(text):


    # Name

    name = re.search(
        r"আমার নাম\s+(.+)",
        text
    )

    if name:

        memory.add(
            "identity",
            "name",
            name.group(1).strip()
        )




    # Call name

    call = re.search(
        r"আমাকে\s+(.+?)\s+বলে ডাকবে",
        text
    )

    if call:

        memory.add(
            "identity",
            "call",
            call.group(1).strip()
        )





    # Skill

    skill = re.search(
        r"(Python|JavaScript|AI|প্রোগ্রামিং)",
        text,
        re.IGNORECASE
    )


    if skill:

        memory.add(
            "skills",
            "skill",
            skill.group(1)
        )





    # Goal

    goal = re.search(
        r"(AI Engineer|এআই ইঞ্জিনিয়ার|Developer)",
        text,
        re.IGNORECASE
    )


    if goal:

        memory.add(
            "goals",
            "goal",
            goal.group(1)
        )





    # Like

    like = re.search(
        r"আমি\s+(.+)\s+পছন্দ করি",
        text
    )


    if like:

        memory.add(
            "preferences",
            "like",
            like.group(1).strip()
        )





    return memory.get()