"""
    Export to json 
"""

import json
from flatlib import const
from s_zodiac import Zodiac

ID_ARIES = 1
ID_TAURUS = 2
ID_GEMINI = 3
ID_CANCER = 4
ID_LEO = 5
ID_VIRGO = 6
ID_LIBRA = 7
ID_SCORPIO = 8
ID_SAGITTARIUS = 9
ID_CAPRICORN = 10
ID_AQUARIUS = 11
ID_PISCES = 12

class Export:
    def __init__(self, angles, houses):
        self.angles = angles
        self.zodiac = self.setZodiac(angles[0]) # angles[0] = Ascendant
        self.houses = houses
    
    def setZodiac(self, asc):
        zodiacById = []
        zodiacById.append(Zodiac(id=ID_ARIES, sign=const.ARIES, asc=asc))
        zodiacById.append(Zodiac(id=ID_TAURUS, sign=const.TAURUS, asc=asc))
        zodiacById.append(Zodiac(id=ID_GEMINI, sign=const.GEMINI, asc=asc))
        zodiacById.append(Zodiac(id=ID_CANCER, sign=const.CANCER, asc=asc))
        zodiacById.append(Zodiac(id=ID_LEO, sign=const.LEO, asc=asc))
        zodiacById.append(Zodiac(id=ID_VIRGO, sign=const.VIRGO, asc=asc))
        zodiacById.append(Zodiac(id=ID_LIBRA, sign=const.LIBRA, asc=asc))
        zodiacById.append(Zodiac(id=ID_SCORPIO, sign=const.SCORPIO, asc=asc))
        zodiacById.append(Zodiac(id=ID_SAGITTARIUS, sign=const.SAGITTARIUS, asc=asc))
        zodiacById.append(Zodiac(id=ID_CAPRICORN, sign=const.CAPRICORN, asc=asc))
        zodiacById.append(Zodiac(id=ID_AQUARIUS, sign=const.AQUARIUS, asc=asc))
        zodiacById.append(Zodiac(id=ID_PISCES, sign=const.PISCES, asc=asc))
        return zodiacById

    # def get_house(self):
    #    print('ok ' + self.house.sign);

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, ensure_ascii=False)