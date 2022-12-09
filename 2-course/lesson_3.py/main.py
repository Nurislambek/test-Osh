# Инкапсуляция
# git clone

#Инкапсуляция - сбор данных в одно место (класс) для работы с ними
#Предоставление пользователя публичного интерфейса



#Неинкапсуляция
"""
def run(a):                     
    print(f'{a} is running')

h='Aziret'
run(h)
"""

#публичный              Types
#защищенный             Types
#закрытый               Types

class Human:
    head=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print(f'{self.name} is running')

h=Human('Aziret', 20)
h.name='SUUUIII'
h._name='Doni'
print(h.name,h._name)
h.run()