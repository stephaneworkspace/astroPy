from datetime import timedelta
import numpy as np

class my_timedelta(timedelta):
    def __str__(self):
        """ Return ° in sign value """
        ms = self.microseconds
        sec = self.seconds
        hours = sec // 3600
        minutes = (sec // 60) - (hours * 60)
        secondes = sec - (minutes * 60) - ((hours * 60) * 60)
        
        if secondes <= 59:
            if ms >= 500000:
                secondes += 1
        else:
            """ secondes = 60 """
            if ms >= 500000:
                secondes = 0
                if minutes <= 59:
                    minutes += 1
                else:
                    minutes = 0
                    hours += 1
                     
        
        days = int(self.days)
        d = self / np.timedelta64(1, 'D').astype(int)
        
        stringDays = int(d.days)
        calc = int(hours + (int(d.days) * 24))

        return "{}°{}'{}''".format(calc, str(minutes).zfill(2), str(secondes).zfill(2))