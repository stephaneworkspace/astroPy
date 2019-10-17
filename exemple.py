#!/usr/bin/env python
import sys
from datetime import datetime as dt, timedelta
from astropyfr import astropy

# print(sys.argv)
date_yyyy_mm_dd = dt.strptime(sys.argv[1], '%Y-%m-%d')
date = dt.strftime(date_yyyy_mm_dd, '%Y/%m/%d')
hour_min = sys.argv[2]
utc = sys.argv[3]
geo_pos_1 = sys.argv[4]
geo_pos_2 = sys.argv[5]

astro = astropyfr.astropyfr(date, hour_min, utc, geo_pos_1, geo_pos_2)
print(astro.get_data())