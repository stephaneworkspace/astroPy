from flatlib import const

class Zodiac:
    def __init__(self, id, sign, asc):
        self.id = id
        self.sign = sign
        self.symbol = self.switchSymbol(sign)
        self.element = self.switchElement(sign)
        self.svg = 'assets/svg/zodiac/' + sign + '.svg'
        self.asc = asc
        self.idByAsc = self.setIdByAsc(asc, id)

    def setIdByAsc(self, asc, id):
        return self.switchAsc(ascSign=asc.sign, id=id)

    def switchAsc(self, ascSign, id):
        switcher = {
            const.ARIES: id,
            const.TAURUS: self.switchAscTaurus(id),
            const.AQUARIUS: self.switchAscAquarius(id)
        }
        return switcher.get(ascSign, '?')
    
    def switchAscTaurus(self, id):
        switcher = {
            2: 1,
            3: 2,
            4: 3,
            5: 4,
            6: 5,
            7: 6,
            8: 7,
            9: 8,
            10: 9,
            11: 10,
            12: 11,
            1: 11 + 1,

        }
        return switcher.get(id, '?')

    def switchAscAquarius(self, id):
        switcher = {
            11: 1,
            12: 2,
            1: 2 + 1,
            2: 2 + 1,
            3: 2 + 3,
            4: 2 + 4,
            5: 2 + 5,
            6: 2 + 6,
            7: 2 + 7,
            8: 2 + 8,
            9: 2 + 9,
            10: 2 + 10,

        }
        return switcher.get(id, '?')

    def switchSymbol(self, sign):
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