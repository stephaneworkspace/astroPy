#!/usr/bin/env python
"""
    Author: Stéphane Bressani
            João Ventura <flatangleweb@gmail.com> -> Flat lib 
              -> https://buildmedia.readthedocs.org/media/pdf/flatlib/latest/flatlib.pdf
            Brandon Craig Rhodes 
              -> https://rhodesmill.org/pyephem/
            Dieter Koch and Dr. Alois Treindl 
              -> https://www.astro.com/swisseph/swephinfo_e.htm
    
    GNU public licence version 2 or later
"""
import sys
from datetime import datetime
from flatlib import aspects
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.protocols import behavior
from s_export import Export

# print(sys.argv)
dateYYYMMDD = datetime.strptime(sys.argv[1], '%Y-%m-%d')
date_str = datetime.strftime(dateYYYMMDD, "%Y/%m/%d")
hour_min = sys.argv[2]
umt = sys.argv[3]

# Build a chart for a date and location
date = Datetime(date_str, hour_min, umt)
pos = GeoPos('46n12', '6e9')
# pos = GeoPos(-71.13, 42.27)

chart = Chart(date, pos, hsys=const.HOUSES_PLACIDUS) #Page 25, livre: Cours complet d'astrologie

# Prepare angles
angles = []
angles.append(chart.get(const.ASC))
angles.append(chart.get(const.DESC))
angles.append(chart.get(const.MC))
angles.append(chart.get(const.IC))

# Prepare houses
houses = []
houses.append(chart.get(const.HOUSE1))
houses.append(chart.get(const.HOUSE2))
houses.append(chart.get(const.HOUSE3))
houses.append(chart.get(const.HOUSE4))
houses.append(chart.get(const.HOUSE5))
houses.append(chart.get(const.HOUSE6))
houses.append(chart.get(const.HOUSE7))
houses.append(chart.get(const.HOUSE8))
houses.append(chart.get(const.HOUSE9))
houses.append(chart.get(const.HOUSE10))
houses.append(chart.get(const.HOUSE11))
houses.append(chart.get(const.HOUSE12))
print(houses[1 - 1])

h = Export(angles=angles, houses=houses)
# h.get_house()
print(h.toJSON())


"""
# Retrieve the Sun and Moon 
sun = chart.get(const.SUN)
moon = chart.get(const.MOON)

# Get the aspect
aspect = aspects.getAspect(sun, moon, const.MAJOR_ASPECTS)
print(aspect)     # <Moon Sun 90 Applicative +00:24:30>

factors = behavior.compute(chart)
for factor in factors:
    print(factor)

print(chart.get(const.MOON))
print(chart.get(const.SUN))
print(chart.get(const.ASC))
print('')
house1 = chart.get(const.HOUSE1)
print(house1)
"""