from datetime import timedelta

class MyTimeDelta(timedelta):
    def __str__(self):
        seconds = self.total_seconds()
        days = seconds // 86400
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        str = '+{}:{}:{}'.format(int(hours), int(minutes), int(seconds))
        return (str)