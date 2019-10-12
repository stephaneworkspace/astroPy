from flatlib import const

class Position():
    """ This class is a tool for positioning over circle 360 """
    def __init__(self, asc):
        self.asc = asc

    def position_cricle_360(self, id):
        pos = ((self.switch_asc(id=id) - 1) * 30.0) - self.asc.signlon
        return pos if pos >= 0 else 360.0 + pos

    def switch_asc(self, id):
        """ Switch case for give a number bettween 1 - 12 by ascendant """
        switcher = {
            const.ARIES: id,
            const.TAURUS: self.switch_asc_taurus(id),
            const.GEMINI: self.switch_asc_gemini(id),
            const.CANCER: self.switch_asc_cancer(id),
            const.LEO: self.switch_asc_leo(id),
            const.VIRGO: self.switch_asc_virgo(id),
            const.LIBRA: self.switch_asc_libra(id),
            const.SCORPIO: self.switch_asc_scorpio(id),
            const.SAGITTARIUS: self.switch_asc_sagittarius(id),
            const.CAPRICORN: self.switch_asc_capricorn(id),
            const.AQUARIUS: self.switch_asc_aquarius(id),
            const.PISCES: self.switch_asc_pisces(id),
        }
        return switcher.get(self.asc.sign, '?')

    def switch_asc_taurus(self, id):
        switcher = {
            const.ID_TAURUS: 1,
            const.ID_GEMINI: 2,
            const.ID_CANCER: 3,
            const.ID_LEO: 4,
            const.ID_VIRGO: 5,
            const.ID_LIBRA: 6,
            const.ID_SCORPIO: 7,
            const.ID_SAGITTARIUS: 8,
            const.ID_CAPRICORN: 9,
            const.ID_AQUARIUS: 10,
            const.ID_PISCES: 11,
            const.ID_ARIES: 11 + 1,

        }
        return switcher.get(id, '?')

    def switch_asc_gemini(self, id):
        switcher = {
            const.ID_GEMINI: 1,
            const.ID_CANCER: 2,
            const.ID_LEO: 3,
            const.ID_VIRGO: 4,
            const.ID_LIBRA: 5,
            const.ID_SCORPIO: 6,
            const.ID_SAGITTARIUS: 7,
            const.ID_CAPRICORN: 8,
            const.ID_AQUARIUS: 9,
            const.ID_PISCES: 10,
            const.ID_ARIES: 10 + 1,
            const.ID_TAURUS: 10 + 2

        }
        return switcher.get(id, '?')

    def switch_asc_cancer(self, id):
        switcher = {
            const.ID_CANCER: 1,
            const.ID_LEO: 2,
            const.ID_VIRGO: 3,
            const.ID_LIBRA: 4,
            const.ID_SCORPIO: 5,
            const.ID_SAGITTARIUS: 6,
            const.ID_CAPRICORN: 7,
            const.ID_AQUARIUS: 8,
            const.ID_PISCES: 9,
            const.ID_ARIES: 9 + 1,
            const.ID_TAURUS: 9 + 2,
            const.ID_GEMINI: 9 + 3
        }
        return switcher.get(id, '?')

    def switch_asc_leo(self, id):
        switcher = {
            const.ID_LEO: 1,
            const.ID_VIRGO: 2,
            const.ID_LIBRA: 3,
            const.ID_SCORPIO: 4,
            const.ID_SAGITTARIUS: 5,
            const.ID_CAPRICORN: 6,
            const.ID_AQUARIUS: 7,
            const.ID_PISCES: 8,
            const.ID_ARIES: 8 + 1,
            const.ID_TAURUS: 8 + 2,
            const.ID_GEMINI: 8 + 3,
            const.ID_CANCER: 8 + 4
        }
        return switcher.get(id, '?')

    def switch_asc_virgo(self, id):
        switcher = {
            const.ID_VIRGO: 1,
            const.ID_LIBRA: 2,
            const.ID_SCORPIO: 3,
            const.ID_SAGITTARIUS: 4,
            const.ID_CAPRICORN: 5,
            const.ID_AQUARIUS: 6,
            const.ID_PISCES: 7,
            const.ID_ARIES: 7 + 1,
            const.ID_TAURUS: 7 + 2,
            const.ID_GEMINI: 7 + 3,
            const.ID_CANCER: 7 + 4,
            const.ID_LEO: 7 + 5
        }
        return switcher.get(id, '?')

    def switch_asc_libra(self, id):
        switcher = {
            const.ID_LIBRA: 1,
            const.ID_SCORPIO: 2,
            const.ID_SAGITTARIUS: 3,
            const.ID_CAPRICORN: 4,
            const.ID_AQUARIUS: 5,
            const.ID_PISCES: 6,
            const.ID_ARIES: 6 + 1,
            const.ID_TAURUS: 6 + 2,
            const.ID_GEMINI: 6 + 3,
            const.ID_CANCER: 6 + 4,
            const.ID_LEO: 6 + 5,
            const.ID_VIRGO: 6 + 6,
        }
        return switcher.get(id, '?')

    def switch_asc_scorpio(self, id):
        switcher = {
            const.ID_SCORPIO: 1,
            const.ID_SAGITTARIUS: 2,
            const.ID_CAPRICORN: 3,
            const.ID_AQUARIUS: 4,
            const.ID_PISCES: 5,
            const.ID_ARIES: 5 + 1,
            const.ID_TAURUS: 5 + 2,
            const.ID_GEMINI: 5 + 3,
            const.ID_CANCER: 5 + 4,
            const.ID_LEO: 5 + 5,
            const.ID_VIRGO: 5 + 6,
            const.ID_LIBRA: 5 + 7,
        }
        return switcher.get(id, '?')

    def switch_asc_sagittarius(self, id):
        switcher = {
            const.ID_SAGITTARIUS: 1,
            const.ID_CAPRICORN: 2,
            const.ID_AQUARIUS: 3,
            const.ID_PISCES: 4,
            const.ID_ARIES: 4 + 1,
            const.ID_TAURUS: 4 + 2,
            const.ID_GEMINI: 4 + 3,
            const.ID_CANCER: 4 + 4,
            const.ID_LEO: 4 + 5,
            const.ID_VIRGO: 4 + 6,
            const.ID_LIBRA: 4 + 7,
            const.ID_SCORPIO: 4 + 8,
        }
        return switcher.get(id, '?')

    def switch_asc_capricorn(self, id):
        switcher = {
            const.ID_CAPRICORN: 1,
            const.ID_AQUARIUS: 2,
            const.ID_PISCES: 3,
            const.ID_ARIES: 3 + 1,
            const.ID_TAURUS: 3 + 2,
            const.ID_GEMINI: 3 + 3,
            const.ID_CANCER: 3 + 4,
            const.ID_LEO: 3 + 5,
            const.ID_VIRGO: 3 + 6,
            const.ID_LIBRA: 3 + 7,
            const.ID_SCORPIO: 3 + 8,
            const.ID_SAGITTARIUS: 3 + 9,
        }
        return switcher.get(id, '?')

    def switch_asc_aquarius(self, id):
        switcher = {
            const.ID_AQUARIUS: 1,
            const.ID_PISCES: 2,
            const.ID_ARIES: 2 + 1,
            const.ID_TAURUS: 2 + 1,
            const.ID_GEMINI: 2 + 3,
            const.ID_CANCER: 2 + 4,
            const.ID_LEO: 2 + 5,
            const.ID_VIRGO: 2 + 6,
            const.ID_LIBRA: 2 + 7,
            const.ID_SCORPIO: 2 + 8,
            const.ID_SAGITTARIUS: 2 + 9,
            const.ID_CAPRICORN: 2 + 10,

        }
        return switcher.get(id, '?')

    def switch_asc_pisces(self, id):
        switcher = {
            const.ID_PISCES: 1,
            const.ID_ARIES: 1 + 1,
            const.ID_TAURUS: 1 + 1,
            const.ID_GEMINI: 1 + 3,
            const.ID_CANCER: 1 + 4,
            const.ID_LEO: 1 + 5,
            const.ID_VIRGO: 1 + 6,
            const.ID_LIBRA: 1 + 7,
            const.ID_SCORPIO: 1 + 8,
            const.ID_SAGITTARIUS: 1 + 9,
            const.ID_CAPRICORN: 1 + 10,
            const.ID_AQUARIUS: 1 + 11,
        }
        return switcher.get(id, '?')