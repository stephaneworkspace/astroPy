"""
    Export to json 
"""

import json
from flatlib import const
from s_zodiac import Zodiac

class Export:
    def __init__(self, angles, houses):
        self.angles = angles
        self.houses = houses
        self.zodiac = self.setZodiac(angles[0]) # angles[0] = Ascendant
    
    def setZodiac(self, asc):
        zodiacById = []
        zodiacById.append(Zodiac(id=const.ID_ARIES, sign=const.ARIES, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_TAURUS, sign=const.TAURUS, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_GEMINI, sign=const.GEMINI, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_CANCER, sign=const.CANCER, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_LEO, sign=const.LEO, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_VIRGO, sign=const.VIRGO, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_LIBRA, sign=const.LIBRA, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_SCORPIO, sign=const.SCORPIO, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_SAGITTARIUS, sign=const.SAGITTARIUS, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_CAPRICORN, sign=const.CAPRICORN, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_AQUARIUS, sign=const.AQUARIUS, asc=asc))
        zodiacById.append(Zodiac(id=const.ID_PISCES, sign=const.PISCES, asc=asc))
        zodiacById.sort(key=lambda x: x.idByAsc)
        return zodiacById

    # def get_house(self):
    #    print('ok ' + self.house.sign);

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, ensure_ascii=False)