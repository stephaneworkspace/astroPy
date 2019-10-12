"""
    Export to json 
"""
import io
import json
from flatlib import const
from astro_py.zodiac import zodiac
from astro_py.house import house

class export:
    def __init__(self, angles, houses):
        self.angles = angles
        self.houses = self.set_house(houses, angles[0])
        self.zodiac = self.set_zodiac(angles[0]) # angles[0] = Ascendant
    
    def set_zodiac(self, asc):
        zodiac_array = []
        zodiac_array.append(zodiac(id=const.ID_ARIES, sign=const.ARIES, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_TAURUS, sign=const.TAURUS, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_GEMINI, sign=const.GEMINI, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_CANCER, sign=const.CANCER, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_LEO, sign=const.LEO, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_VIRGO, sign=const.VIRGO, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_LIBRA, sign=const.LIBRA, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_SCORPIO, sign=const.SCORPIO, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_SAGITTARIUS, sign=const.SAGITTARIUS, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_CAPRICORN, sign=const.CAPRICORN, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_AQUARIUS, sign=const.AQUARIUS, asc=asc))
        zodiac_array.append(zodiac(id=const.ID_PISCES, sign=const.PISCES, asc=asc))
        zodiac_array.sort(key=lambda x: x.id_by_asc)
        return zodiac_array

    def set_house(self, houses, asc):
        house_array = []
        for i in houses:
            house_array.append(house(house=i, asc=asc))
        return house_array
        


    def to_json(self):
        json_dumps = json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, ensure_ascii=False)
        return json_dumps