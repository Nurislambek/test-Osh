"""
class Human:
    #атрибут уровня класс
    head=1
    head=2
    #конструктор класса
    def __init__(self,name,age):
        self.name=name
        self.age=age

#объект класса
human=Human('Nurislam',14)
print(human.name,human.age)
human2=Human('Elmyrza',14)
print(human2.name,human2.age)
"""

class Car:
    motor=1
    def __init__(self,marka,model,country):
        self.marka=marka
        self.model=model
        self.country=country
    def __str__(self):
        return f'marka of car its {self.marka}\n' \
               f'model of car its {self.model}\n' \
               f'country of car its {self.country}'
    
car1=Car('Bmw','X5', 'Germany')
car2=Car('Mersedes','gtr63','Germany')
car3=Car('Lexus','lx570','Japan')
print(car1,car2,car3)