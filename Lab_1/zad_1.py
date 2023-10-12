from term import Term
from day import Day

term1 = Term(Day.MON, 8, 30)
term2 = Term(Day.TUE, 9, 45, 30)
term3 = Term(Day.TUE, 11, 15, 90)
print(term1)                             # Ma się wypisać: "Poniedziałek 8:30 [90]"
print(term2)                             # Ma się wypisać: "Wtorek 9:45 [30]"
print(term3)                             # Ma się wypisać: "Wtorek 11:15 [90]"
print("term1 < term2:", term1 < term2)   # Ma się wypisać True
print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
print("term1 > term2:", term1 > term2)   # Ma się wypisać False
print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
print("term2 == term2:", term2 == term2) # Ma się wypisać True
print("term2 == term3:", term2 == term3) # Ma się wypisać False
term4 = term3 - term1                    # Tworzy termin, którego:
                                         # - termin rozpoczęcia jest taki jak dla 'term1',
                                         # - czas trwania to różnica minut pomiędzy terminem zakończenia 'term3' (Wtorek 11:15), a godziną rozpoczęcia 'term1' (Poniedziałek 8:30)
print(term4)                             # Ma się wypisać "Poniedziałek 8:30 [1605]"
        