import random
firstNames = ("Thomas", "Daniel", "James", "Aaron", "Tommy", "Terrell", "Jack", "Joseph", "Samuel", "Quinn", "Hunter", "Vince", "Young", "Ian", "Erving", "Leo")
lastNames = ("Smith", "Johnson", "Williams", "Kline","Brown", "Garcia", "Jones", "Miller", "Davis","Williams", "Alves", "Sobronsky", "Hall", "Murphy", "Morris")
class profile:
    def __init__ (self):
        self.name = firstNames[random.randrange(0,len(firstNames))] + " " + lastNames[random.randrange(0,len(lastNames))]
        self.years = 2020
        self.ppg = random.randrange(10, 380)/10
        self.apg = random.randrange(10,120)/10
        self.rpg = random.randrange(10,280)/10
        self.bpg = random.randrange(5,60)/10
        self.spg = random.randrange(0,30)/10
        self.tpg = random.randrange(1,40)/10
        self.age = random.randrange(18,24)

    def getStats (self):
        output = {"Age:" : self.age,
        "name" : self.name,
        "points per game" : self.ppg,
        "assists per game" : self.apg,
        "rebounds per game" : self.rpg,
        "blocks per game" : self.bpg,
        "steals per game" : self.spg,
        "turnovers per game" : self.tpg,}
        return output
    def incrementAge (self):
        self.age += 1
