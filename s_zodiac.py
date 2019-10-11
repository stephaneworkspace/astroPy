from flatlib import const

class Zodiac:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.symbol = self.switchSymbol(nom)
        self.element = self.switchElement(nom)
        self.svg = 'assets/svg/zodiac/' + nom + '.svg'

    def switchSymbol(self, nom):
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
        return switcher.get(nom, '?')
    
    def switchElement(self, nom):
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
        return switcher.get(nom, '?')