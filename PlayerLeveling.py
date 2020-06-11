class Novice:

    # when level changes check stats
    # create a when statement specifically for each stat change
    # for now work with only one player stat

    player = {
        'name': '',
        'class': '',
        'lvl': 1,
        'xp': 0,
        'lvlNext': 25,
        'stats': {'str': 1,
                  'dex': 1,
                  'int': 1,
                  'atk': [5, 12],
                  'hp': 20,
                  'maxHp': 20},
        'weapons': []
    }


'''

COMMENTED OUT UNTIL USED 

def Adept():
    player = {
        'name': '',
        'class': '',
        'lvl': 25,
        'xp': 1000,
        'lvlNext': 50,
        'stats': {'str': 3,
                  'dex': 3,
                  'int': 3,
                  'atk': [15, 36],
                  'hp': 60,
                  'maxHp': 60},
        'weapons': []
    }


def Grandmaster():
    player = {
        'name': '',
        'class': '',
        'lvl': 50,
        'xp': 1000,
        'lvlNext': 75,
        'stats': {'str': 9,
                  'dex': 9,
                  'int': 9,
                  'atk': [45, 108],
                  'hp': 180,
                  'maxHp': 180},
        'weapons': []
    }


def Champion():
    player = {
        'name': '',
        'class': '',
        'lvl': 75,
        'xp': 1000,
        'lvlNext': 100,
        'stats': {'str': 27,
                  'dex': 27,
                  'int': 27,
                  'atk': [135, 324],
                  'hp': 540,
                  'maxHp': 540},
        'weapons': []
    }


def Visionary():
    player = {
        'name': '',
        'class': '',
        'lvl': 100,
        'xp': 0,
        'lvlNext': 'Maxed',
        'stats': {'str': 81,
                  'dex': 81,
                  'int': 81,
                  'atk': [405, 972],
                  'hp': 1620,
                  'maxHp': 1620},
        'weapons': []
    }



'''

