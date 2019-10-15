from astro_py.zodiac import zodiac
from flatlib import const

class astro_py_text:
    def __init__(self, zodiac): #angles, houses, planets):
        self.zodiac = zodiac
    
    def text_zodiac(self):
        zodiac_text_array = []
        for i in self.zodiac:
            zt = zodiac_text(i)
            zodiac_text_array.append(zt)
        return zodiac_text_array
    
class zodiac_text_struct:
    def __init__(self, pictogramme):
        self.pictogramme = pictogramme

class zodiac_text_pictograme:
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        
    def setTitre(self, titre):
        self.titre = titre
        
    def setContenu(self, contenu):
        self.contenu = contenu

class zodiac_text:
    def __init__(self, zodiac):
        self.sign = zodiac.sign
        self.struct = zodiac_text_struct(self.switch_zodiac_pictogramme(zodiac.id))
        
    def switch_zodiac_pictogramme(self, id):
        switcher = {
            const.ID_ARIES: self.text_pictogramme_belier(),
            const.ID_TAURUS: self.text_pictogramme_autre(),
            const.ID_GEMINI: self.text_pictogramme_autre(),
            const.ID_CANCER: self.text_pictogramme_autre(),
            const.ID_LEO: self.text_pictogramme_autre(),
            const.ID_VIRGO: self.text_pictogramme_autre(),
            const.ID_LIBRA: self.text_pictogramme_autre(),
            const.ID_SCORPIO: self.text_pictogramme_autre(),
            const.ID_SAGITTARIUS: self.text_pictogramme_autre(),
            const.ID_CAPRICORN: self.text_pictogramme_autre(),
            const.ID_AQUARIUS: self.text_pictogramme_autre(),
            const.ID_PISCES: self.text_pictogramme_autre(),
        }
        return switcher.get(id, '?')
    
    def text_pictogramme_belier(self):
        f = open('assets/zodiac_01_belier_pictogramme.dat', 'r')
        content = f.read()
        f.close()
        return zodiac_text_pictograme('Le pictogramme du Bélier', content)
        
    def text_pictogramme_autre(self):
        return zodiac_text_pictograme('Titre autre', 'Autre')