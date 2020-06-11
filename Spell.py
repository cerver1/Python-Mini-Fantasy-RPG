class Spell:

    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints


fyre = Spell("Fyre", 5)
electrine = Spell("Electrine", 5)
flux = Spell("Flux", 5)
lux = Spell("Lux", 5)
wynd = Spell("Wynd", 5)

Spells = dict({
    "fyre": fyre,
    "electrine": electrine,
    "flux": flux,
    "lux": lux,
    "wynd": wynd
})
