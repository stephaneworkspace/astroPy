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
        zodiacById.append(Zodiac(ID_ARIES, const.ARIES))
        zodiacById.append(Zodiac(ID_TAURUS, const.TAURUS))
        zodiacById.append(Zodiac(ID_GEMINI, const.GEMINI))
        zodiacById.append(Zodiac(ID_CANCER, const.CANCER))
        zodiacById.append(Zodiac(ID_LEO, const.LEO))
        zodiacById.append(Zodiac(ID_VIRGO, const.VIRGO))
        zodiacById.append(Zodiac(ID_LIBRA, const.LIBRA))
        zodiacById.append(Zodiac(ID_SCORPIO, const.SCORPIO))
        zodiacById.append(Zodiac(ID_SAGITTARIUS, const.SAGITTARIUS))
        zodiacById.append(Zodiac(ID_CAPRICORN, const.CAPRICORN))
        zodiacById.append(Zodiac(ID_AQUARIUS, const.AQUARIUS))
        zodiacById.append(Zodiac(ID_PISCES, const.PISCES))
        return zodiacById

    # def get_house(self):
    #    print('ok ' + self.house.sign);

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, ensure_ascii=False)