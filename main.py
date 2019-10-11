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
import time
from datetime import datetime
import flatlib 
from flatlib import aspects
from flatlib import const # https://github.com/flatangle/flatlib/blob/master/flatlib/const.py
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


#print(sys.argv)

dateYYYMMDD = datetime.strptime(sys.argv[1], '%Y-%m-%d')
date_str = datetime.strftime(dateYYYMMDD, "%Y/%m/%d")
hour_min = sys.argv[2]
umt = sys.argv[3]
# Build a chart for a date and location
date = Datetime(date_str, hour_min, umt)
pos = GeoPos('38n32', '8w54')
#pos = GeoPos(-71.13, 42.27)

chart = Chart(date, pos, hsys=const.HOUSES_PLACIDUS) #Page 25

# Retrieve the Sun and Moon 
sun = chart.get(const.SUN)
moon = chart.get(const.MOON)

# Get the aspect
aspect = aspects.getAspect(sun, moon, const.MAJOR_ASPECTS)
print(aspect)     # <Moon Sun 90 Applicative +00:24:30>

# date = Datetime('2015/03/13', '17:00', '+00:00')
# Write 'Hello, World' to standard output.
print('Hello, World')

from flatlib.protocols import behavior

factors = behavior.compute(chart)
for factor in factors:
    print(factor)

print(chart.get(const.MOON))
print(chart.get(const.SUN))
print(chart.get(const.ASC))
print('')
house1 = chart.get(const.HOUSE1)
print(house1)