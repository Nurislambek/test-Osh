class A:...

a=1
print(type(a))


# class Human:
#     head=1
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f'name is {self.name}\n'

class SuperHero: 
    people='people' 
    fly = True 
    def __init__(self, name, nickname, superpower, health_points, catchphrase): 
        self.name = name 
        self.nickname = nickname 
        self.superpower = superpower 
        self.health_points = health_points 
        self.catchphrase = catchphrase 
    def nameHero(self): 
        print("Name hero is", self.name) 
     
    def squarehealth_points(self): 
        print("Health_points: ",self.health_points * 2) 
 
    def __str__(self) -> str: 
        return f"Status hero:\nNikname hero - {self.nickname}\nSuperpower hero - {self.superpower}\nhealth_points hero - {self.health_points}" 
         
    def __len__(self): 
        return len(self.catchphrase) 

class Hero1(SuperHero):
    h=1
    def __init(self, name, nickname, superpower, health_points, catchphrase, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
    def print_name_hero(self):
        print(f'{self.health_points **2}')
        self.fly=True
    def fly_true():
        print('fly in the True_phrases')

class Hero2(SuperHero):
    j=1
    def __init(self, name, nickname, superpower, health_points, catchphrase, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)        
        self.fly = fly
    def print_name_hero(self):
        print(f'{self.health_points **2}')
        self.fly=True
    def fly_true():
        print('fly in the True_phrases')

class Hero3(SuperHero):
    l=1
    def __init(self, name, nickname, superpower, health_points, catchphrase, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)        
        self.fly = fly
    def print_name_hero(self):
        print(f'{self.health_points **2}')
        self.fly=True
    def fly_true():
        print('fly in the True_phrases')