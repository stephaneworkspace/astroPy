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
from datetime import datetime as dt, timedelta
from flatlib import aspects
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.protocols import behavior
from astro_py.export import export
from astro_py.component.my_timedelta import my_timedelta

class astro_py:
  def __init__(self, date, hour_min, utc):
    # Build a chart for a date and location
    date = Datetime(date, hour_min, utc)
    pos = GeoPos('46n12', '6e9') # Geneva, Switzerland
    chart = Chart(date, pos, hsys=const.HOUSES_PLACIDUS, IDs=const.LIST_OBJECTS) #Page 25, livre: Cours complet d'astrologie
    
    # Prepare angles
    angles = []
    angles.append(chart.get(const.ASC))
    angles.append(chart.get(const.IC))
    angles.append(chart.get(const.DESC))
    angles.append(chart.get(const.MC))

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

    # Prepare planets
    planets = []
    planets.append(chart.get(const.SUN))
    planets.append(chart.get(const.MOON))
    planets.append(chart.get(const.MERCURY))
    planets.append(chart.get(const.VENUS))
    planets.append(chart.get(const.MARS))
    planets.append(chart.get(const.JUPITER))
    planets.append(chart.get(const.SATURN))
    planets.append(chart.get(const.URANUS))
    planets.append(chart.get(const.NEPTUNE))
    planets.append(chart.get(const.PLUTO))
    planets.append(chart.get(const.NEPTUNE))
    planets.append(chart.get(const.CHIRON))
    planets.append(chart.get(const.NORTH_NODE))
    planets.append(chart.get(const.SOUTH_NODE))
    planets.append(chart.get(const.PARS_FORTUNA))
    self.data = export(angles=angles, houses=houses, planets=planets)
    
  def get_data(self):
    """ Export json of all datas """
    return self.data.to_json()




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