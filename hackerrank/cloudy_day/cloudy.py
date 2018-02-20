#!/usr/bin/env python

class Town:

    __slots__ = ['position', 'population']

    def __init__(self, pos, pop):
        self.position = pos
        self.population = pop

    def __lt__(self, other):
        return ((self.position < other.position) or
                (self.position == other.position and
                 self.population < other.population))

    def __repr__(self):
        return "Town %d %d" % (self.position, self.population)

class Cloud:

    __slots__ = ['position', 'length']

    def __init__(self, pos, length):
        self.position = pos
        self.length = length

    def __lt__(self, other):
         return ((self.position < other.position) or
                 (self.position == other.position and
                  self.length < other.length))

    def __repr__(self):
        return "Cloud %d %d" % (self.position, self.length)

def compare(town, cloud):
    if town.position < cloud.position:
        return -1
    if town.position > cloud.position + cloud.length:
        return 1
    return 0

def selectTowns(towns, clouds):
    sunny = []
    single = []
    c_idx = t_idx = 0
    while t_idx < len(towns) and c_idx < len(clouds):
        comp = compare(towns[t_idx], clouds[c_idx])
        if comp < 0:
            sunny.append(towns[t_idx])
            t_idx += 1
        elif comp > 0:
            c_idx += 1
        elif isSingleCloudTown(towns[t_idx], clouds, c_idx):
            single.append(towns[t_idx])
            t_idx += 1
        else:
            t_idx += 1

    sunny.extend(towns[t_idx:])
    return (sunny, single)

def isSingleCloudTown (town, clouds, c_idx):
    count = 0
    town_pos = town.position
    while c_idx < len(clouds):
        cloud_pos = clouds[c_idx].position
        if town_pos < cloud_pos:
            break
        elif town_pos < cloud_pos + clouds[c_idx].length:
            count += 1
            if count > 1:
                return False
        c_idx += 1

    return count == 1

def sumPopulation(towns):
    total = 0
    for town in towns:
        total += town.population
    return total

def maximumToUncover(towns, clouds):
    t_idx = c_idx = mx = 0
    while t_idx < len(towns) and c_idx < len(clouds):
        comp = compare(towns[t_idx], clouds[c_idx])
        if comp < 0:
            t_idx += 1
        elif comp > 0:
            c_idx += 1
        else:
            mx = max(mx, coveredPopulation(clouds[c_idx], towns, t_idx))
            c_idx += 1
            t_idx += 1
    return mx

def coveredPopulation(cloud, towns, t_idx):
    population = 0
    while t_idx < len(towns):
        if compare(towns[t_idx], cloud) != 0:
            break
        population += towns[t_idx].population
        t_idx += 1
    return population

from time import time

if __name__ == "__main__":
    print "%s - %s" % (time(), "Reading input")
    n = int(raw_input().strip())
    p = map(long, raw_input().strip().split(' '))
    x = map(long, raw_input().strip().split(' '))
    m = int(raw_input().strip())
    y = map(long, raw_input().strip().split(' '))
    r = map(long, raw_input().strip().split(' '))

    print "%s - %s" % (time(), "Building arrays")
    towns = [Town(pos, pop) for (pos, pop) in zip(x, p)]
    clouds = [Cloud(pos - rng, 2 * rng) for (pos, rng) in zip(y, r)]

    print "%s - %s" % (time(), "Sorting arrays")
    towns.sort()
    clouds.sort()

    print "%s - %s" % (time(), "Selecting towns")
    (sunnyTowns, singleCloudTowns) = selectTowns(towns, clouds)
    print "%s - %d sunny, %d single-cloud towns" % (time(), len(sunnyTowns), len(singleCloudTowns))
    print "%s - %s" % (time(), "Summing sunny population")
    sunnyPopulation = sumPopulation(sunnyTowns)
    print "%s - %s" % (time(), "Calculating maximum population to uncover")
    maxUncover = maximumToUncover(singleCloudTowns, clouds)
    print (sunnyPopulation + maxUncover)
    print "%s - %s" % (time(), "Done!")
