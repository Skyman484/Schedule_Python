import unittest
from day import Day
from term import Term
from lesson import Lesson
from timetable import Timetable
from action import Action
timex = Timetable()
class Test_TestLesson(unittest.TestCase):
    def test_moveDay(self):
        t = Timetable()
        lekcja_1 = Lesson(t, Term(Day.MON, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(lekcja_1.earlierDay())
        lekcja_2 =  Lesson(t, Term(Day.MON, 9, 0), "Angielski", "Stanisław Polak", 2)
        self.assertTrue(lekcja_2.laterDay())
        lesson_3 = Lesson(t, Term(Day.FRI, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(lesson_3.laterDay())
        lesson_4 = Lesson(t, Term(Day.MON, 15, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(lesson_4.earlierDay())
        lesson = Lesson(t, Term(Day.TUE, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertTrue(lesson.laterDay())
        self.assertEqual(str(lesson), str(Lesson(t, Term(Day.WED, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)))
    
    def test_moveTime(self):
        t = Timetable()
        lekcja_1 = Lesson(t, Term(Day.TUE, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(lekcja_1.earlierTime())
        lekcja_2 = Lesson(t, Term(Day.FRI, 17, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(lekcja_2.earlierTime())
        lekcja_3 = Lesson(t, Term(Day.WED, 17, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertTrue(lekcja_3.laterTime())
        lekcja_4 = Lesson(t, Term(Day.FRI, 15, 30), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(lekcja_4.laterTime())
        lekcja_5 = Lesson(t, Term(Day.SUN, 18, 30), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertFalse(lekcja_5.laterTime())

class Timetable1Test(unittest.TestCase):
    def test_timetable(self):
        lesson = Lesson(timex, Term(Day.THU, 8, 0, 90), "Programowanie", "Stanisław Polak", 2)
        lesson_1 = Lesson(timex, Term(Day.THU, 8, 0, 90), "Programowanie", "Stanisław Polak", 2)
        self.assertTrue(timex.put(lesson))
        self.assertFalse(timex.put(lesson))
        self.assertFalse(timex.put(lesson_1))
        self.assertEqual(timex.get(lesson.term), lesson)
        actList = timex.parse(["d-"])
        self.assertEqual(actList, [Action.DAY_EARLIER])
        timex.perform(actList)
        self.assertEqual(lesson.term._Term__day, Day.WED)
        lesson2 = Lesson(timex, Term(Day.THU, 11, 0), "Matma", "Matematyk", 1)
        self.assertTrue(timex.put(lesson2))
        actList = timex.parse(["d+", "d-"])
        self.assertEqual(actList, [Action.DAY_LATER, Action.DAY_EARLIER])
        timex.perform(actList)
        self.assertEqual(lesson2.term._Term__day, Day.WED)
        self.assertEqual(lesson.term._Term__day, Day.THU)
        lesson3 =  Lesson(timex, Term(Day.WED, 11, 0), "Angielski", "Brytyjczyk", 1)
        self.assertFalse(timex.put(lesson3))
if __name__ == '__main__':
    unittest.main(exit=False)
    print(timex)