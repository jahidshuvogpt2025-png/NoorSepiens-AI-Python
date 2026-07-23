from core.long_memory import get_memory



def generate_profile():

    memory = get_memory()


    card = """
🤖 NoorSepiens AI Profile
━━━━━━━━━━━━━━

"""


    if "name" in memory:

        card += f"""
👤 Name:
{memory['name']}
"""


    if "skill" in memory:

        card += f"""
💻 Skill:
{memory['skill']}
"""


    if "goal" in memory:

        card += f"""
🎯 Goal:
{memory['goal']}
"""



    card += """

━━━━━━━━━━━━━━
🧠 Personal AI Memory Active
"""


    return card
