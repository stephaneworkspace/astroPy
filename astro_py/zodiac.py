from flatlib import const
from astro_py.position import Position

class Zodiac():
    """ This class represents the zodiac """

    def __init__(self, id, sign, asc):
        """ Creates an zodiac class """
        self.id = id
        self.sign = sign
        self.symbol = self.switchSymbol(sign)
        self.element = self.switchElement(sign)
        self.svg = 'assets/svg/zodiac/' + sign + '.svg'
        # self.asc = asc
        position = Position(asc)
        self.idByAsc = position.switchAsc(id)
        self.posCircle360 = position.positionCricle360(id)

    def switchSymbol(self, sign):
        """ Font icon of the sign """
        switcher = {
            const.ARIES: '♈',
            const.TAURUS: '♉',
            const.GEMINI: '♊',
            const.CANCER: '♋',
            const.LEO: '♌',
            const.VIRGO: '♍',
            const.LIBRA: '♎',
            const.SCORPIO: '♏',
            const.SAGITTARIUS: '♐',
            const.CAPRICORN: '♑',
            const.AQUARIUS: '♒',
            const.PISCES: '♑'
        }
        return switcher.get(sign, '?')
    
    def switchElement(self, sign):
        """ Element of zodiac """
        switcher = {
            const.ARIES: 'Feu',
            const.TAURUS: 'Terre',
            const.GEMINI: 'Air',
            const.CANCER: 'Eau',
            const.LEO: 'Feu',
            const.VIRGO: 'Terre',
            const.LIBRA: 'Air',
            const.SCORPIO: 'Eau',
            const.SAGITTARIUS: 'Feu',
            const.CAPRICORN: 'Terre',
            const.AQUARIUS: 'Air',
            const.PISCES: 'Eau'
        }
        return switcher.get(sign, '?')