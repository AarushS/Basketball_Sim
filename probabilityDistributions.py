import math
import random as rnd
import matplotlib.pyplot as plt


# Define PDF
def pdf(x, v):
    return ((math.e ** (-x/2)) * (x ** (v/2 - 1))) / ((2 ** (v/2)) * math.gamma(v/2))

# Define CDF using riemann sum for indefinite integration
def cdf(x, q, v):
    scalar = x/q
    sum = 0
    for n in range(1,q):
        sum += pdf(n*scalar, v)
    return(sum*scalar)

# Use CDF Map to find approx inverse of CDF
def inverse_transform(seed, map):
        minindex = 0
        minProximity = abs(map[0][1] - seed)
        for i in map:
            if (abs(i[1]-seed) < minProximity):
                minindex = map.index(i)
                minProximity = abs(i[1]-seed)
        out = map[minindex][0]
        return out


class probabilityDistributions:
    def __init__(self, peak):
        self.v = peak + 2
        self.cdfmap = []

        i = 1
        self.cdfmap.append((0, cdf(0, 100, self.v)))
        while abs(self.cdfmap[-1][1] - 1) > .001:
            y = cdf((i/100), 100, self.v)
            x = i/100
            self.cdfmap.append( (x,y) )
            i += 1

    def getCDFMap(self):
        out = self.cdfmap[:]
        return out

    def getValue(self, seed = rnd.randrange(0,1001)/1000):
        return inverse_transform(seed, self.cdfmap)

    def plotHistrogram(self, points = 500, plotCurve = False):
        genNums = []
        for _ in range(points):
            genNums.append(inverse_transform(rnd.randrange(0,1001)/1000, self.cdfmap))

        if plotCurve:
            listX, listY = [], []
            for i in range(0,int(max(genNums) + 1) * 100):
                listX.append(i/100)
                listY.append(pdf(listX[-1], self.v))
            plt.plot(listX, listY)

        plt.hist(genNums, density = True, bins = 15)
        plt.show()


#testing
'''
object = probabilityDistributions(9.5)

print(object.getValue())
object.plotHistrogram(plotCurve = True)
'''
