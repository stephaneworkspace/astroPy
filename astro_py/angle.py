from flatlib import const
from astro_py.position import position
from astro_py.component.my_timedelta import my_timedelta

class angle():
    def __init__(self, angle, asc):
        # self._angle = angle
        self.id = self.switch_current_id(angle.id)
        self.name = angle.id
        # self.id_house = house.id
        self.sign = angle.sign
        self.sign_pos = str(my_timedelta(0, angle.signlon * 3600))
        # self.signlon = house.signlon
        pos = position(asc)
        id_by_asc = pos.switch_current_sign_to_id(angle.sign)
        self.pos_circle_360 = pos.position_circle_360_object(id_by_asc, angle.signlon)
        
    def switch_current_id(self, name):
        """ For house.py, current sign -> id sign """
        switcher = {
            const.ASC: 1,
            const.DESC: 3,
            const.MC: 4,
            const.IC: 2,
        }
        return switcher.get(name, '?')