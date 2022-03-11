from classes.person import Person
from datetime import date

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pier = Person('Pierre', 'Alain', date(1998, 2, 4))
    megane = Person('Meg', 'Troll', date(1978, 3, 12))
    pier + megane
    print(pier)