player = {
  'name' : '',
  'class':'',
  'lvl': 1,
  'xp': 0,
  'lvlNext' : 25,       
  'stats' : {'str': 1,
              'dex' : 1,
              'int' : 1,
              'atk' : [5, 12],
              'hp' : 20,
              'maxHp' : 20},
  'weapons':[]      
  }
class Spell:
   def __init__(self, name, hitpoints):
    self.name = name
    self.hitpoints = hitpoints

fyre = Spell("Fyre", 5)
electrine = Spell("Electrine", 5)
flux = Spell("Flux", 5)
lux = Spell("Lux", 5)
wynd = Spell("Wynd", 5)

def getPlayerInfo():
  print('What is your name?')
  player['name'] = input()
  print('Hi,', player['name'] + "!")
  print('What is your class?')
  print('Mage | Swordsman')
  player['class'] =input().casefold()
  if 'mage' in player.values():
    print('Ah, a mage. You can cast spells.')   
  else:
    player['class'] == 'swordsman'
    print('A strong swordsman! You can use almost any style of sword with ease.')

def getPlayerWeapons():
  if player['class'] == 'mage':
    print('What two spells can you cast? Say "OK" when you\'re done')
    print('Fyre | Electrine | Flux | Lux | Wynd')
    while True:
      weaponChoices = player['weapons']
      spellSelections = input().casefold()
      if spellSelections == 'Fyre' or 'Electrine' or 'Flux' or 'Lux' or 'Wynd':
         weaponChoices.append(spellSelections)
         #can I use a class here?
       # 
      else:
       print('That isn\'t a valid spell!')
      if len(weaponChoices) == 2:
        print('You have chosen', weaponChoices[0], 'and', weaponChoices[1], '.')
        break
 
getPlayerInfo()
getPlayerWeapons()
import time
print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
print("Our journey begins here...")