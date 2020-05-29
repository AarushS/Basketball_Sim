import random


firstNames = ("Thomas", "Daniel", "James", "Aaron", "Tommy", "Terrell", "Jack", "Joseph", "Samuel", "Quinn", "Hunter", "Vince", "Young", "Ian", "Erving", "Leo")
lastNames = ("Smith", "Johnson", "Williams", "Kline","Brown", "Garcia", "Jones", "Miller", "Davis","Williams", "Alves", "Sobronsky", "Hall", "Murphy", "Morris")

# Verifies statistics are not negative
f = lambda x : 0 if (x < 0) else x


def improvementFunction(age, maxMu):
    return (maxMu/-30) * (age - 17) * (age - 30)


class profile:
    def __init__ (self):
        self.name = firstNames[random.randrange(0,len(firstNames))] + " " + lastNames[random.randrange(0,len(lastNames))]
        self.years = 2020
        self.ppg = [f(round( random.gauss(10.5, 2.4), 1))]
        self.apg = [f(round(random.gauss(5.2, 2.4), 1))]
        self.rpg = [f(round(random.gauss(4.7, 2.4), 1))]
        self.bpg = [f(round(random.gauss(1, .8), 1))]
        self.spg = [f(round(random.gauss(.9, 1.2), 1))]
        self.tpg = [f(round(random.gauss(1.8, .5), 1))]
        self.age = random.randrange(18,24)
        self.fgp = [f(round(random.gauss(39.2, 5.4), 1))]
        self.tpp = [f(round(random.gauss(28.7, 6), 1))]

    def getStats (self):
        output = {"Age:" : self.age,
        "name" : self.name,
        "points per game" : self.ppg[-1],
        "assists per game" : self.apg[-1],
        "rebounds per game" : self.rpg[-1],
        "blocks per game" : self.bpg[-1],
        "steals per game" : self.spg[-1],
        "turnovers per game" : self.tpg[-1],
        "field goal percentage" : self.fgp[-1],
        "three point percentage" : self.tpp[-1]}
        return output

    def incrementAge (self):
        self.age += 1

    def updateStats (self):
        self.ppg.append(f(round(self.ppg[-1] + random.gauss(improvementFunction(self.age, 5 - 2 * 1.8), 1.8), 1)))
        self.apg.append(f(round(self.apg[-1] + random.gauss(improvementFunction(self.age, self.apg[-1] * 2 - 6), 1.5), 1)))
        self.rpg.append(f(round(self.rpg[-1] + random.gauss(improvementFunction(self.age, self.rpg[-1] * 1.5 - 3), 1.5), 1)))
        self.bpg.append(f(round(self.bpg[-1] + random.gauss(improvementFunction(self.age, self.bpg[-1] * 2 - 1), .5), 1)))
        self.spg.append(f(round(self.spg[-1] + random.gauss(improvementFunction(self.age, self.spg[-1] * 2 - 1), .5), 1)))
        self.tpg.append(f(round(self.tpg[-1] + random.gauss(improvementFunction(self.age, 2.5 - .5), .5), 1)))
        self.fgp.append(f(round(self.fgp[-1] + random.gauss(improvementFunction(self.age, 10 - 3), 2.5), 1)))
        self.tpp.append(f(round(self.tpp[-1] + random.gauss(improvementFunction(self.age, 8 - 3), 1.9), 1)))
