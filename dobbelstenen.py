import random
def dobbelsteen_nummers():
    nummer = 0
    nummer += random.randint(1,6)
    return nummer


def dobbelsteen_level():
    levels = ['hard','medium','easy']
    nummer = random.choice(levels)
    return nummer