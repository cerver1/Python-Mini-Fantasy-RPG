from random import randint


def DiceRoll(sides):
    assurance = randint(1, sides)

    if randint(1, 2) == 1:
        fate = True
    else:
        fate = False

    return assurance, fate


def rollResponse(roll):
    if roll[1]:
        return "Mysterious magic is afoot"
    else:
        if roll[0] in range(1, 5):
            return "That didn't go as planned"
        elif roll[0] in range(5, 9):
            return "That sort of worked"
        elif roll[0] in range(9, 13):
            return "You are able to execute"
        else:
            return "your dice fell off the table"

