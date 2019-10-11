"""
    Export to json 
"""

import json

class Export:
    def __init__(self, angles, houses):
        self.angles = angles
        self.houses = houses

    # def get_house(self):
    #    print('ok ' + self.house.sign);

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, ensure_ascii=False)