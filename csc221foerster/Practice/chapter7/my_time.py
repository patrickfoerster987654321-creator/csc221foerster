class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return f'{self.hours}:{self.minutes:02d}:{self.seconds:02d}'

    def increment(self, seconds):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + seconds
        h = total_seconds // 3600
        total_seconds = total_seconds - (h * 3600)
        m = total_seconds // 60
        s = total_seconds - (m * 60)
        return f'{h}:{m:02d}:{s:02d}'

    def after(self, other):
        if self.hours > other.hours:
            return True
        if self.hours < other.hours:
            return False

        if self.minutes > other.minutes:
            return True
        if self.minutes < other.minutes:
            return False

        if self.seconds > other.seconds:
            return True
        return False

