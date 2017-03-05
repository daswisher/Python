#!/usr/bin/env python
import json

continentsFile = open("continents.json","r")
continents = json.loads(continentsFile.read())
world = dict()
for country in continents:
	continent = continents[country]
	if continent in world:
		world[continent].append(country)
	else:
		world[continent] = [country]
file1 = open("countries.json", "w")
json.dump(world, file1, separators=(',', ': '), indent=4)
file1.close()
