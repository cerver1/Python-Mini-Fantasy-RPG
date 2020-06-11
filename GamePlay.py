from PlayerLeveling import Novice
from Spell import Spells
from Melee import Blades
from Narrative import Introduction


def getPlayerInfo():

    Introduction()

    print('\nWhat is your name?')
    Novice.player['name'] = input()
    print('Hi,', Novice.player['name'] + "!")
    getPlayerClass()


def getPlayerClass():
    print('What is your class?')
    print('Mage | Swordsman')
    Novice.player['class'] = input().casefold()

    if 'mage' in Novice.player.values():
        print('Ah, a mage. You can cast spells.')
        getPlayerSpells()
    elif 'swordsman' in Novice.player.values():
        print('A strong swordsman! You can use almost any style of sword with ease.')
        getPlayerWeapons()
    else:
        print("Hmmm something seems to have gone wrong!")
        getPlayerClass()


def getPlayerSpells():
    print("What two spells can you cast? Say 'OK' when you're done")
    print('Fyre | Electrine | Flux | Lux | Wynd')
    while True:
        weapon_choices = Novice.player['weapons']
        spell_input = input().casefold()
        if spell_input in Spells:
            weapon_choices.append(spell_input)
        else:
            print('That isn\'t a valid spell!')
        if len(weapon_choices) == 2:
            print('Ahhhh {} and {} powerful indeed.'.format(weapon_choices[0], weapon_choices[1]))
            break


def getPlayerWeapons():
    print("What two weapons can you wield? Say 'OK' when you're done")
    print('Machete | Dao | Rapier | Katana | Zweihander')
    while True:
        weapon_choices = Novice.player['weapons']
        blade_input = input().casefold()
        if blade_input in Blades:
            weapon_choices.append(blade_input)
        else:
            print('That isn\'t a valid weapon!')
        if len(weapon_choices) == 2:
            print('Ahhhh {} and {} skillful indeed.'.format(weapon_choices[0], weapon_choices[1]))
            break
