import enum

class Day(enum.Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7
    
    def __str__(self):
        days = {
            1: "Poniedziałek",
            2: "Wtorek",
            3: "Środa",
            4: "Czwartek",
            5: "Piątek",
            6: "Sobota",
            7: "Niedziela"
        }
        return days[self.value]

    def difference(self, day):
        diff = day.value - self.value
        if diff > 3:
            diff = diff - 7
        if diff < -3:
            diff = diff + 7
        return diff

def nthDayFrom(n, day):
    #print("i am in day")
    my_day = day.value + n
    if my_day > 7:
        my_day = my_day - 7
    if my_day < 1:
        my_day = my_day + 7
    return Day(my_day)


