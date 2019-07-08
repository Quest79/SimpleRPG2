# Charactor class for creating charactors and its subclasses, monsters, heros,
# npcs etc.
from equiptment import Equiptment as Equip
from toolz import pTools
from random import randint

mTen = 10
attackTableRange = 1000
p = pTools()
critM = 1.5
printhelp = 0


class Charactor(object):
    def __init__(self, name='', prof='', health=100, mana=10, armor=100, strength=10, level=1, alive=True, miss=5, dodge=5, parry=5, block=5, crit=15):
        """name='', prof='', health=100, mana=10, armor=100, strength=10, level=1, alive=True,
                 miss=5, dodge=5, parry=5, block=5, crit=15"""
        self.name = name
        self.prof = prof
        self.health = health
        self.mana = mana
        self.armor = armor
        self.strength = strength
        self.level = level
        self.alive = alive
        self.miss = miss
        self.dodge = dodge
        self.parry = parry
        self.block = block
        self.crit = crit
        self.blkdmg = self.strength / 2 + 5
        self.mis = self.miss + .1

    def armorDR(self):
        """Returns the damage reduction from armor."""
        self.dmgred = self.armor / (self.armor + 400 + 85 * self.level)
        return round(self.dmgred, 4)

    def defenseDR(self):
        """Returnes the damage reduction from defense."""
        self.defense = 45 + self.level * 5
        self.defdr = self.defense * 0.16 / 100
        return round(self.defdr, 4)

    def damageReduction(self):
        """This returns the total damage reduction."""
        self.dmgRD = self.armorDR() + self.defenseDR()
        return round(self.dmgRD, 4)

    def damageTaken(self, dmg):
        """This returns damaged taken after damage reduction."""
        self.dmgTaken = (1 - self.damageReduction()) * dmg
        return round(self.dmgTaken)

    def damageBlocked(self, dmg):
        blkdmgtaken = dmg - self.blkdmg
        if blkdmgtaken < 0:
            blkdmgtaken = 0
            return blkdmgtaken
        else:
            return blkdmgtaken

    def dmgOut(self, swing):
        damout = swing + (self.strength / 3)
        return damout

    # Attack table range calculations.
    # Determines tables out of 1000 table points (100 would be percent)
    def missRange(self):
        self.missrange = 10, p.mulT(self.miss, mTen)
        return self.missrange

    def dodgeRange(self):
        self.dodgerange = p.mulT(self.mis,
                                 mTen), p.mulT(self.miss + self.dodge, mTen)
        return self.dodgerange

    def parryRange(self):
        self.parryrange = p.mulT(self.mis + self.dodge, mTen), p.mulT(
            self.miss + self.dodge + self.parry, mTen)
        return self.parryrange

    def blockRange(self):
        self.blockrange = p.mulT(
            self.mis + self.dodge + self.parry,
            mTen), p.mulT(self.miss + self.dodge + self.parry + self.block,
                          mTen)
        return self.blockrange

    def critRange(self):
        self.critrange = p.mulT(
            self.mis + self.dodge + self.parry + self.block, mTen), p.mulT(
                self.miss + self.dodge + self.parry + self.block + self.crit,
                mTen)
        if self.critrange[1] > attackTableRange:
            self.critrange = p.mulT(
                self.mis + self.dodge + self.parry + self.block,
                mTen), attackTableRange
            return self.critrange
        else:
            return self.critrange

    def hitRange(self):
        self.hitrange = p.mulT(
            self.mis + self.dodge + self.parry + self.block + self.crit,
            mTen), attackTableRange
        if self.hitrange[0] > attackTableRange:
            print("Hit value pushed off hit table:")
            return self.hitrange
        else:
            return self.hitrange

    def getHitType(self):
        n = pTools()
        self.mi = self.miss * mTen
        self.do = self.dodge * mTen
        self.pa = self.parry * mTen
        self.bl = self.block * mTen
        self.cr = self.crit * mTen
        self.swing = randint(10, attackTableRange)

        if n.betTup(self.swing, self.missRange()):
            return "Miss"
        elif n.betTup(self.swing, self.dodgeRange()):
            return "Dodge"
        elif n.betTup(self.swing, self.parryRange()):
            return "Parry"
        elif n.betTup(self.swing, self.blockRange()):
            return "Block"
        elif n.betTup(self.swing, self.critRange()):
            return "Critical"
        elif n.betTup(self.swing, self.hitRange()):
            return "Hit"
        else:
            return "Error, Reached no result. How.. " + str(self.swing)


e = Charactor('Bear', 'mob', 100, 10, 100, 15, 1, True,
              miss=5, dodge=5, parry=5, block=10, crit=25)
h = Charactor('Tim', 'Mage', 100, 10, 100, 10, 1, True,
              miss=5, dodge=5, parry=5, block=10, crit=25)

sword = Equip('sword', 1.0, 10, 20, 5, 0, "The First Sword")
axe = Equip('axe', 1.2, 12, 18, 10, 0, "The First Sword")

# region Print Information
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
for i in range(10):
    # e.getHitType()
    print(e.getHitType())
print("------------------------------------")
print("MISS - " + str(e.missRange()))
print("DODG - " + str(e.dodgeRange()))
print("PARY - " + str(e.parryRange()))
print("BLCK - " + str(e.blockRange()))
print("CRIT - " + str(e.critRange()))
print("NHIT - " + str(e.hitRange()))
print("------------------------------------")
print("------------------------------------")
print("My name is:       " + str(h.name))
print("My armor DR is:   " + str(h.armorDR()))
print("My defense DR is: " + str(h.defenseDR()))
print("My total is:      " + str(h.damageReduction()))
print("------------------------------------")
print("If hit for 10000, I take " + str(h.damageTaken(10000)) + " damage.")
print("------------------------------------")
print("My weapon is a:          " + str(sword.etype))
print("My weapon is called:     " + str(sword.name))
print("It has a high damage of: " + str(sword.highdmg))
print("It has a low damage of:  " + str(sword.lowdmg))
print("Averges to:              " + str(sword.getDamageAvg()))
for i in range(2):
    print("Attack --> " + str(sword.getRandDmg()))
print("------------------------------------")
print("++++++++++++++++++++++++++++++++++++")
print("------------------------------------")
# endregion

for x in range(0):
    attack_type = e.getHitType()
    swing_damage = sword.getRandDmg()
    # assert swing_damage > 0, 'Swing was less than 1. How bad can you be?'
    if attack_type == "hit":
        print("WE DONE HIT IT")
    if attack_type == "missed":
        print("We missed")
    if attack_type == "dodged":
        print("Dodged out hit")
    if attack_type == "perried":
        print("Parried our attack")
    if attack_type == "blockd":
        print("We got blocked. Damage done: " +
              str(e.damageBlocked(e.damageTaken(swing_damage))))
        # hitp = hitp - e.damageBlocked(e.damageTaken(swing_damage))
    if attack_type == "crithit":
        print("Critical strike of " + str(e.damageTaken(swing_damage * critM)))
        # hitp = hitp - (e.damageTaken(swing_damage * critM))
        # print(hitp)
    print(attack_type)
    print(e.swing)
    print("++++++++++++++++++++++++++++++++++++")

hmax = h.health

while not h.alive:

    if h.health > 0:
        attack_type = e.getHitType()
        swing_damage = sword.getRandDmg()
        print(attack_type + " with roll of: " + str(e.swing))

        if attack_type == "Hit":
            h.health = h.health - e.damageTaken(swing_damage)
        elif attack_type == "Critical":
            print("Critical strike of " +
                  str(e.damageTaken(swing_damage * critM)))
            h.health = h.health - (e.damageTaken(swing_damage * critM))
        elif attack_type == "Block":
            print(
                str(e.blkdmg) + " got blocked. Damage done: " +
                str(e.damageBlocked(e.damageTaken(swing_damage))))
            h.health = h.health - e.damageBlocked(e.damageTaken(swing_damage))
        elif attack_type == "Miss":
            pass
        elif attack_type == "Dodge":
            pass
        elif attack_type == "Parry":
            pass

        # print("Raw Damage: " + str(swing_damage))
        print("After DmgR: " + str(e.damageTaken(swing_damage)))
        print(h.name + " health out of " + str(hmax) + ": ->" + str(h.health))
        print("++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++")

    elif h.health <= 0:
        print("*** IM DEAD ***")
        h.alive = False

while h.alive:
    e_dmg = axe.getRandDmg()
    h_dmg = sword.getRandDmg()
    e_type = e.getHitType()
    h_type = h.getHitType()
    ask = input("Would you like to attack? y/n: ")

    if ask == "y":
        pass

    if ask == "n":
        break
