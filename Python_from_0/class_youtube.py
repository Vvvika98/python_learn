#создадим собственный класс 

class Ork:          #монстр в ммо рпг
    def __init__(self,*, level: int) -> None:     #метод инициализации класса, там два подчеркивания спереди и сзади, они определяют как будет вести себя объект класса с разными конструкциями языка
        self.level = level   #ключевое слово self - это !экземпляр! класса, атрибутов мб много поэтому используем ключевое слово. Его мы передаем в метод класса 
        self.health_points = 100 * level        #создем атрибут очки здоровья 
        self.attack_power = 100 * level         #атрибут/свойства сила атаки 

#2 сделаем метод атак у класса 
    def attack(self):        #self - экземпляр
        print(f"Ork attacks with {self.attack_power} power")


#метод для взаимодействия классов с различными встроенными функциями и ключевыми словами
#дандрметоды
    def __str__(self):
        return f"Ork (level: {self.level}, hp: {self.health_points})"

#вывод для 2-----------------------------------------------------------
ork = Ork(level = 2) #создаем экземпляр класса Орк 
# print(ork.level)
# print(ork.health_points)
print(ork.attack_power) 
ork.attack()           #вызываем метод атаки здесь self = ork


# -----------------------------------------------------------

#атрибутами (свойствами) экземпляра класса можно управлять, напр. можно уровень поднять
ork.level += 1
print(ork.level)

#вывод для 3-----------------------------------------------------------
print(ork)

#-----------------------------------------------------------
#НАСЛЕДОВАНИЕ 
class Ork:         
    def __init__(self, level: int) -> None:     #метод инициализации класса, там два подчеркивания спереди и сзади, они определяют как будет вести себя объект класса с разными конструкциями языка
        self.level = level   #ключевое слово self - это !экземпляр! класса, атрибутов мб много поэтому используем ключевое слово. Его мы передаем в метод класса 
        self.health_points = 100 * level        #создем атрибут очки здоровья 
        self.attack_power = 10 * level         #атрибут/свойства сила атаки 


    def attack(self):        #self - экземпляр
        print(f"Ork attacks with {self.attack_power} power")


#метод для взаимодействия классов с различными встроенными функциями и ключевыми словами
#дандрметоды
    def __str__(self):
        return f"Ork (level: {self.level}, hp: {self.health_points})"


#НАПИШЕМ НОВЫЙ КЛАСС - НОВОЕ СУЩЕСТВО - ЭЛЬФ

# class Elf:
#     def __init__(self,*, level: int) -> None:
#         self.level = level 
#         self.health_points = 50 * level        #создем атрибут очки здоровья 
#         self.attack_power = 15 * level         #атрибут/свойства сила атаки 

#     def attack(self):        #self - экземпляр
#         print(f"Elf attacks with {self.attack_power} power")

#     def __str__(self):
#         return f"Elf (level: {self.level}, hp: {self.health_points})"

    
    #DRY - НЕ КОПИРОВАТЬ САМОГО СЕБЯ И ДЛЯ ЭТОГО СУЩЕСТВУЕТ НАСЛЕДОВАНИЕ У КЛАССОВ. КЛАСС Character - ПОДЛОЖКА для написания других персонажей
    
    class Character: #НАСЛЕДУЕМЫЙ КЛАСС
        def __init__(self, *, level: int) -> None:
            self.level = level 
            #т.к. ХП у персонажей разные пишем
            self.health_points = self.base_health_points * level
            self.attack_power = self.base_attack_power * level

        #метод атаки
        def attack(self):      
            print(f"{self.character_name} attacks with {self.attack_power} power")

        #метод печатающий персонажа в консоли 
        def __str__(self):
            return f"{self.character_name} (level: {self.level}, hp: {self.health_points})"

    #ТЕПЕРЬ ОТНАСЛЕДУЕМСЯ ОТ ОБЩЕГО КЛАССА И СОЗДАДИМ ПЕРСОНАЖЕЙ - ОРКА И ЭЛЬФА

    class Ork(Character):
        #определяем атрибуты класса
        base_health_points = 100
        base_attack_power = 10
        character_name = "Ork"

    class Elf(Character):
        #определяем атрибуты класса
        base_health_points = 50
        base_attack_power = 15
        character_name = "Elf"

        #в классе Эльфа переопредеяем метод атак в классе НАСЛЕДНИКА
        def attack(self):
            print("This method is from class-inheritor")


#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------


#делаем бой персонажей 

    class Character: #НАСЛЕДУЕМЫЙ КЛАСС
        def __init__(self, *, level: int) -> None:
            self.level = level 
            #т.к. ХП у персонажей разные пишем
            self.health_points = self.base_health_points * level
            self.attack_power = self.base_attack_power * level

        #метод атаки передаем цель, по котрой идет атака 
        def attack(self, *, target: "Character") -> None:      
            print(
                f"{self.character_name} attacks {target.character_name} ({target.health_points} health_points)"  #существо нападает на цель и у этой цели столько хп, 
                f" with {self.attack_power} power."   #атакуается с такой силой
                )
            target.health_points -= self.attack_power   #отнимаем от хп цели силу атаки нападающего
            print(f"After attack {target.character_name} hp has {target.health_points}") #после атаки у цели осталось столько хп

        #метод что существо еще живо
        def is_alive (self) -> bool:
            return self.health_points > 0

        #метод печатающий персонажа в консоли 
        def __str__(self):
            return f"{self.character_name} (level: {self.level}, hp: {self.health_points})"

    

    class Ork(Character):
        #определяем атрибуты класса
        base_health_points = 100
        base_attack_power = 10
        character_name = "Ork"

    class Elf(Character):
        #определяем атрибуты класса
        base_health_points = 50
        base_attack_power = 15
        character_name = "Elf"


    #БОЙ
    def fight(*, character_1: Character, character_2: Character) -> None:
        while character_1.is_alive() and character_2.is_alive():
            character_1.attack(target = character_2)
            if character_2.is_alive():
                character_2.attack(target = character_1)

        print(f" Character 1: {character_1} is_alive: {character_1.is_alive()} ")
        print(f" Character 2: {character_2} is_alive: {character_2.is_alive()}")

#ИНИЦИАЛИЗИРУЕМ ДВА ИНСТАНСА (ЭКЗЕМПЛЯРА, ОБЪЕКТА КЛАССА)
    ork = Ork(level = 1)
    elf = Elf(level = 1)

#и запустим их в драку
    fight(character_1 = ork, character_2 = elf)



#Усложним!!!!!!!!!!!!!

class Character: #НАСЛЕДУЕМЫЙ КЛАСС
    def __init__(self, *, level: int) -> None:
        self.level = level 
            #т.к. ХП у персонажей разные пишем
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

        #метод атаки передаем цель, по котрой идет атака 
    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage = self.attack_power)    #получить урон = сила атаки

        #метод получения урона 
    def got_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage     #здоровье (хп) минус урон

        #метод что существо еще живо
    def is_alive (self) -> bool:
        return self.health_points > 0

        #свойство класса загоняется под декоратор
    @property 
        #защита
    def defence(self) -> int:  
        defence = self.base_defence * self.level #защита = базовая защита * на уровень
        return defence
        
        #определяем % хп (здоровья)
    def health_points_percent(self):   
        return 100 * self.health_points / self.max_health_points   #хп * на максимальное хп

        #определяем максимальное хп
    @property 
    def max_health_points(self) -> int:
        return self.level * self.base_health_points         #уровень * базовое хп

    


class Ork(Character):
        #определяем атрибуты класса
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"
    base_defence = 15
    #определяем ПЕРКИ - суперспособности 
    @property 
        #защита
    def defence(self) -> int: 
        defence = super().defence     #супер - значит обращаемся к НАСЛЕДУЕМОМУ КЛАССУ и там вызываем декоратор проперти дефенс 
        if self.health_points < 50:
            defence *= 3    #используем перк (суперспособность)
        
        return defence


class Elf(Character):
        #определяем атрибуты класса
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"
    base_defence = 10
 #определяем ПЕРКИ - суперспособности, переопределяем атаку у эльфа
    def attack(self, *, target: "Character") -> None:
        attack_power = self.attack_power          #сила атаки = сила атаки в наследуемом классе       
        if target.health_points_percent() < 30:   #если % здоровья после атаки меньше 30
            attack_power = self.attack_power * 3  #сила атаки увеличивается на 3
        # print(f"Elf attack_power = {attack_power}")
        target.got_damage(damage=attack_power)    #получение урона, где урон = как раз эта сила акати троекратная


#НОВЫЙ БОЙ 
def fight(*, character_1: Character, character_2: Character) -> None:
        while character_1.is_alive() and character_2.is_alive():
            character_1.attack(target = character_2)
            if character_2.is_alive():
                character_2.attack(target = character_1)

        print(f" Character 1: {character_1} is_alive: {character_1.is_alive()} ")
        print(f" Character 2: {character_2} is_alive: {character_2.is_alive()}")


ork_1 = Ork(level=1)
elf_1 = Elf(level=1)

fight(character_1=ork_1, character_2=elf_1)


#инкапсуляция - скрытие внутренней логики внутри класса, наружу д.б. выведены всего несколько методов
#полиморфирз - переопределение конструкции язык для каждого класса (этим занимаются дандер методы где __ и __)
#наследование - создаем класс наслдник и уже в наследуемых класс не дублируем свой код


