import csvParser as psr
import math
import pants
import csv
import matplotlib.pyplot as plt

nodes = psr.csvParser('open_pubs.csv')

print('Pubs: ', len(nodes))


def distance(a, b):  # Retourne la distance en kilomètre
    distance = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)) / 1000
    return distance


world = pants.World(nodes, distance)

solver = pants.Solver()

solutions = solver.solutions(world)

bestDistance = -1
for solution in solutions:
    if(solution.distance < bestDistance or bestDistance < 0):
        bestDistance = solution.distance
        bestTour = solution.tour

print('Distance parcourue : ' + str(bestDistance) + 'km')

xArray = []
yArray = []
for node in bestTour:
    xArray.append(node[0])
    yArray.append(node[1])
plt.plot(xArray, yArray)
plt.show()
