from datetime import timedelta
import numpy as np

class my_timedelta(timedelta):
    def __str__(self):
        """ Return ° in sign value """
        sec = self.seconds
        hours = sec // 3600
        minutes = (sec // 60) - (hours * 60)
        secondes = sec - (minutes * 60) - ((hours * 60) * 60)
        
        days = int(self.days)
        d = self / np.timedelta64(1, 'D').astype(int)
        
        stringDays = int(d.days)
        calc = int(hours + (int(d.days) * 24))

        return "{}°{}'{}''".format(calc, str(minutes).zfill(2), str(secondes).zfill(2))