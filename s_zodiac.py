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
            const.GEMINI: self.switchAscGemini(id),
            const.CANCER: self.switchAscCancer(id),
            const.AQUARIUS: self.switchAscAquarius(id)
        }
        return switcher.get(ascSign, '?')
    
    def switchAscTaurus(self, id):
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

    def switchAscGemini(self, id):
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

    def switchAscCancer(self, id):
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

    def switchAscAquarius(self, id):
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