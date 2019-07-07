from random import randint

mTen = 100
attbl = 10000


class Equiptment(object):
    def __init__(self, etype='', speed=0, lowdmg=1, highdmg=2, strength=0, armor=0, name=''):
        """etype='', speed=0, lowdmg=1, highdmg=2, strength=0, armor=0, name=''"""
        self.etype = etype
        self.speed = speed
        self.lowdmg = lowdmg
        self.highdmg = highdmg
        self.strength = strength
        self.armor = armor
        self.name = name

    def getDamageAvg(self):
        self.avgdmg = (self.highdmg + self.lowdmg) / 2.0
        return self.avgdmg

    def getRandDmg(self):
        self.normRND = randint(self.lowdmg, self.highdmg)
        return self.normRND

    def getRound(self, num, dec):
        self.rounded = round(num, dec)
        return self.rounded
