from flatlib import const
from astro_py.position import position
from astro_py.component.my_timedelta import my_timedelta

class planet:
    def __init__(self, planet, asc):
        # self._planet = planet
        self.id = planet.id
        # self.id_house = house.id
        self.sign = planet.sign
        self.sign_pos = str(my_timedelta(0, planet.signlon * 3600))
        # self.signlon = house.signlon
        pos = position(asc)
        id_by_asc = pos.switch_current_sign_to_id(planet.sign)
        self.pos_circle_360 = pos.position_circle_360_object(id_by_asc, planet.signlon)
        self.svg = 'assets/svg/planet/' + planet.id + '.svg'
        