from flatlib import const
from astro_py.component.my_timedelta import my_timedelta

def house(self, house):
    def __init__(self, house):
        self._house = house
        self.id_house = house.id
        self.sign = house.sign
        self.signlon = house.signlon
        self.signlon_format = str(my_timedelta(0, house.signlon * 3600))
    """
    print(chart.getHouse(const.HOUSE1).signlon)
    print(chart.getHouse(const.HOUSE1).id)
    print(chart.getHouse(const.HOUSE1).sign)
    print(chart.getHouse(const.HOUSE1).size)
    """