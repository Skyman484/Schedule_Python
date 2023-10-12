from day import Day
from term import Term

class Lesson():
    def time(self, termin) -> bool:
        if termin._Term__day == Day.SAT or termin._Term__day == Day.SUN or (termin._Term__day == Day.FRI and termin._Term__hour >= 17):
            self.__fullTime = False
        else:
            #print("i am in time, in true")
            self.__fullTime = True
            
    def __init__(self, timetable, term:Term, name:str, teacherName:str, year:int):
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        if term._Term__day == Day.SAT or term._Term__day == Day.SUN or (term._Term__day == Day.FRI and term._Term__hour >= 17):
            self.__fullTime = False
        else:
            self.__fullTime = True
        self.__timetable = timetable

    #TERM
    @property
    def term(self):
        return self.__term
        
    @term.setter
    def term(self, term):
        self.__term = term    
    #NAME    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name
    #TEACHER    
    @property
    def teacherName(self):
        return self.__teacherName
        
    @teacherName.setter
    def teacherName(self, teacherName):
        self.__teacherName = teacherName
    #YEAR    
    @property
    def year(self):
        return self.__year
        
    @year.setter
    def year(self, year):
        self.__year = year
        
    #FULL_TIME    
    @property
    def fullTime(self):
        return self.__fullTime

    @fullTime.setter
    def fullTime(self, fullTime):
        if type(fullTime) == type(True):
            self.__fullTime = fullTime
            return True
        return False

    def __str__(self):
        if self.__year == 1:
            rok = 'Pierwszy rok'
        elif self.__year == 2:
            rok = 'Drugi rok'
        elif self.__year == 3:
            rok = 'Trzeci rok'
        elif self.__year == 4:
            rok = 'Czwarty rok'
        elif self.__year == 5:
            rok = 'Piąty rok'

        return f"""{self.__name} ({self.__term})\n{rok} studiów {"stacjonarnych" if self.__fullTime else "niestacjonarnych"}\nProwadzący: {self.__teacherName}"""
    
    def kolizja(termin, fullTime):
        if fullTime == True and termin._Term__day != Day.FRI:
            if termin._Term__hour < 8 or termin._Term__hour > 18 or (termin._Term__hour == 8 and termin._Term__minute < 0) or (termin._Term__hour == 18 and termin._Term__minute > 30):
                return True
        elif fullTime == True and termin._Term__day == Day.FRI:
            if termin._Term__hour < 8 or termin._Term__hour > 15 or (termin._Term__hour == 8 and termin._Term__minute < 0) or (termin._Term__hour == 15 and termin._Term__minute > 30):
                return True
        elif fullTime == False and termin._Term__day != Day.FRI:
            if termin._Term__hour < 8 or termin._Term__hour > 18 or (termin._Term__hour == 8 and termin._Term__minute < 0) or (termin._Term__hour == 18 and termin._Term__minute > 30):
                return True
        elif fullTime == False and termin._Term__day == Day.FRI:
            if termin._Term__hour < 17 or termin._Term__hour > 18 or (termin._Term__hour == 17 and termin._Term__minute < 0) or (termin._Term__hour == 18 and termin._Term__minute > 30):
                return True

        return False

    def move(self, dist, znak, name):
        from timetable import Timetable
        old_day = self.__term._Term__day
        old_hour = self.__term._Term__hour
        old_minute = self.__term._Term__minute
        old_duration = self.__term._Term__duration
        old_fullTime = self.__fullTime
        if znak == 1:
            from day import nthDayFrom
            #print("i am in earlier day")
            self.__term._Term__day = nthDayFrom(-1,self.__term._Term__day)
            self.time(self.__term)
            if self.__fullTime != old_fullTime:
                return False
        elif znak == 2:
            #print("I am here")
            from day import nthDayFrom
            self.__term._Term__day = nthDayFrom(1,self.__term._Term__day)
            self.time(self.__term)
            if self.__fullTime != old_fullTime:
                #print("am i in fulltime !=")
                return False
        else:
            newminutes = (self.__term._Term__hour * 60) + self.__term._Term__minute + dist
            self.__term._Term__hour = newminutes // 60 # o ktorej sie koncza. Jest to po to aby nie okazało sie ze zajecia trwaja dluzej niz jest to mozliwe
            self.__term._Term__minute = newminutes % 60
            self.__term._Term__duration = dist

        if self.__timetable.can_be_transferred_to(self.__term, self.__fullTime, name) == True:
            #print("i am here at the end of kolizja")
            return True
        else:
            self.__term._Term__day = old_day
            self.__term._Term__hour = old_hour
            self.__term._Term__minute = old_minute
            self.__term._Term__duration = old_duration
            return False

    def earlierDay(self, name=''):
        return self.move(0,1,name)

    def laterDay(self, name=''):
        #print("later day execute")
        return self.move(0,2, name)

    def earlierTime(self, name=''):
        return self.move(-90, 0, name)

    def laterTime(self, name=''):
        return self.move(90, 0, name)

# lesson = Lesson(Term(Day.TUE, 9, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
# print(lesson); #"""Programowanie skryptowe (Wtorek 9:40-11:10)
#                  Drugi rok studiów stacjonarnych
#                 Prowadzący: Stanisław Polak
#                """
