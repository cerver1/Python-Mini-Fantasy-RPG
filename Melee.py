class Blade:

    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints


Machete = Blade("Machete", 5)
Dao = Blade("Dao", 5)
Rapier = Blade("Rapier", 5)
Katana = Blade("Katana", 5)
Zweihander = Blade("Zweihander", 5)

Blades = dict({
    'machete': Machete,
    'dao': Dao,
    'rapier': Rapier,
    'katana': Katana,
    'zweihander': Zweihander
})
