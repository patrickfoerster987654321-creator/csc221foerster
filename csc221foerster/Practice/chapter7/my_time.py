class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def print_time(self):
        print(f'{self.hours}:{self.minutes:02d}:{self.seconds:02d}')
    def increment(self, seconds):
        self.seconds = seconds + self.seconds

        while self.seconds >= 60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1

        while self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1
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

