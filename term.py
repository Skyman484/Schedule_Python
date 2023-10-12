from day import Day
from math import floor
class Term:
    def __init__(self, day, hour, minute, duration=90):
        self.__day = day
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration
    #zad1
    # def __str__(self):
    #     return f"{self.__day} {self.__hour}:{self.__minute} [{self.__duration}]"

    #zad2
    def __str__(self):
        return f"{self.__day} {self.__hour}:{self.__minute}-{self.__hour + ((self.__minute + self.__duration) // 60)}:{(self.__minute + self.__duration) % 60}"

    @property
    def get_day(self):
        return self.__day

    @get_day.setter
    def get_day(self, d):
        self.__day = d

    @property
    def get_hour(self):
        return self.__hour

    @get_hour.setter
    def get_hour(self, h):
        self.__hour = h

    @property
    def get_minute(self):
        return self.__minute

    @get_minute.setter
    def get_minute(self, m):
        self.__minute = m
    
    @property
    def get_duration(self):
        return self.__duration

    @get_duration.setter
    def get_duration(self, du):
        self.__duration = du

    @classmethod
    def fromInt(cls, minutes:int):
        return Term(Day(floor(minutes/1440)+1), floor(minutes/60) - floor(minutes/1440)*24, minutes % 60)

    def earlierThan(self, termin):
        if self.__day.difference(termin.__day) > 0  or self.__hour < termin.__hour or (self.__hour == termin.__hour and self.__minute < termin.__minute):
            return True
        else:
            return False

    def laterThan(self, termin):
        if self.__day.difference(termin.__day) < 0 or self.__hour > termin.__hour or (self.__hour == termin.__hour and self.__minute > termin.__minute):
            return True
        else:
            return False

    def equals(self, termin):
        if self.__day.difference(termin.__day) == 0 and self.__hour == termin.__hour and self.__minute == termin.__minute and self.__duration == termin.__duration:
            return True
        else:
            return False

    # overload < (less than) operator
    def __lt__(self, termin):
        return self.earlierThan(termin)

    # overload > (greater than) operator
    def __gt__(self, termin):
        return self.laterThan(termin)

     # overload <= (less than or equal to) operator
    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    # overload >= (greater than or equal to) operator
    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    # overload == (equal to) operator
    def __eq__(self, termin):
        return self.equals(termin)

    # overload - operator
    def __sub__(self, termin):
        return Term(termin.__day, termin.__hour, termin.__minute, ( self.__hour*60 + self.__minute ) - (termin.__hour*60 + termin.__minute))
    
