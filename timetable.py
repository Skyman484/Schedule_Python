from typing import List
from term import Term
from lesson import Lesson
from day import Day
from action import Action
from math import floor
import re

class Timetable(object):
    name_of_subject = '' 
    def __init__(self):
        self.__list = []

    def can_be_transferred_to(self, term: Term, fullTime: bool, name='') -> bool:
        self.name_of_subject = name
        if self.busy(term) == False:
            #print("here you are")
            if Lesson.kolizja(term, fullTime) == False:
                #print("NICE")
                return True
            # else:
            #     print("kolizja is damaged")
        else:
            #print("oh no")
            return False

    def busy(self, term: Term) -> bool:
        for lesson in self.__list:
            #print("To jest w busy" + self.name_of_subject)
            if self.get(term) != None and lesson._Lesson__term == term and lesson._Lesson__name != self.name_of_subject:
                return True
        return False

    def put(self, lesson: Lesson) -> bool:
        self.name_of_subject = lesson._Lesson__name
        #print(self.name_of_subject)
        if(self.can_be_transferred_to(lesson._Lesson__term, lesson._Lesson__fullTime)):
            for i in range(len(self.__list)):
                if  self.__list[i]._Lesson__name == lesson._Lesson__name and self.__list[i]._Lesson__term == lesson._Lesson__term:
                    return False
            #print("dodałem")
            self.__list.append(lesson)
            return True
        return False

    def parse(self, actions: List[str]) -> List[Action]:
        
        tablica_napisow = []
        for action in actions:
            if action == "d+":
                tablica_napisow.append(Action.DAY_LATER)
            elif action == "d-":
                tablica_napisow.append(Action.DAY_EARLIER)
            elif action == "t+":
                tablica_napisow.append(Action.TIME_LATER)
            elif action == "t-":
                tablica_napisow.append(Action.TIME_EARLIER)
        
        return tablica_napisow

    def perform(self, actions: List[Action]):
        i = 0
        #print(self.name_of_subject)
        for a in range (len(actions)):
            #print("Lista: ", self.__list[i])
            if actions[a] == Action.DAY_EARLIER:
                self.__list[i].earlierDay(self.__list[i]._Lesson__name)
            elif actions[a] == Action.DAY_LATER:
                self.__list[i].laterDay(self.__list[i]._Lesson__name)
            elif actions[a] == Action.TIME_EARLIER:
                self.__list[i].earlierTime(self.__list[i]._Lesson__name)
            elif actions[a] == Action.TIME_LATER:
                self.__list[i].laterTime(self.__list[i]._Lesson__name)
                
            i = (i + 1) % len(self.__list)
        self.name_of_subject = ''

    def get(self, term: Term) -> Lesson:
        for lesson in self.__list:
            if lesson._Lesson__term == term:
                #print("lekcja jest na liscie")
                return lesson
        return None
    def czyszczenie(self):
        self.name_of_subject = ''

    @staticmethod
    def align(string):
        if(len(string) > 20):
            return string[:20]
        else:
            i = (20-len(string))/2
            if(i % 1):
                i = floor(i)
                return " "*i + string + " "*(i+1)
            else:
                i = int(i)
                return " "*i + string + " "*i

    def __str__(self):
        out = " "*20
        for i in range(1,8):
            out += "*" + Timetable.align(str(Day(i)))
            
        out += "\n" + "*"*(8*20+7) + "\n"
        start = Term.fromInt(480)
        begin = f'{start._Term__hour}:{start._Term__minute}0'
        # print(begin)
        if start._Term__minute + 90 % 60 == 0:
            ending = f'{start._Term__hour + 90 //60}:{start._Term__minute + 90 % 60}0'
        else:
            ending = f'{start._Term__hour + 90 //60}:{start._Term__minute + 90 % 60}'
        # print(ending)
        for i in range(0,8):
            time = str(begin) + "-" + str(ending)
            out += Timetable.align(time)
            for j in range(0,7):
                lesson = self.get(Term.fromInt(start._Term__hour * 60 + (90 * i)+ start._Term__minute +1440*j))
                if(lesson == None):
                    out += "*" + " "*20 
                else:
                    out += "*" + Timetable.align(lesson.name)

            if start._Term__minute + (90 * (i+1)) % 60 == 0 and (start._Term__minute + (90 * (i+1)) + 90 ) % 60 != 0:
                begin = f'{start._Term__hour + (90 * (i+1)) // 60}:{start._Term__minute + (90 * (i+1)) % 60}0'
                ending = f'{(start._Term__hour + (90 * (i+1)) // 60) + ((start._Term__minute + (90 * (i+1)) % 60) + 90 ) // 60}:{(start._Term__minute + (90 * (i+1)) + 90 ) % 60}'
        
            if (start._Term__minute + (90 * (i+1)) + 90 ) % 60 == 0 and start._Term__minute + (90 * (i+1)) % 60 != 0:
                begin = f'{start._Term__hour + (90 * (i+1)) // 60}:{start._Term__minute + (90 * (i+1)) % 60}'
                ending = f'{(start._Term__hour + (90 * (i+1)) // 60) + ((start._Term__minute + (90 * (i+1)) % 60) + 90 ) // 60}:{(start._Term__minute + (90 * (i+1)) + 90 ) % 60}0'
            
            out += "\n" + "*"*(8*20+7) + "\n"
        return out