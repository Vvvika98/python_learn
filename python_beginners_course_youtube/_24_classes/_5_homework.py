# задание
# Скопируйте код из предыдущего урока.
# Имплементируйте следующий функционал:
# 1. После убийства персонажа, уровень того, кто убил, повышается на 1.
# 2. Максимальный уровень персонажа - 3.
# 3. При повышении уровня персонажа, происходит отхил, и персонажу прибавляется половина от максимального количества хп.
# 4. Уровень должен повышаться в функции fight
# После имплементации, и запуска функции fight, при вызове должно вывестись:
# Ork is alive Ork (level: 2, hp: 140)
# Elf is dead Elf (level: 1, hp: -4)

# решение (классы очень вариативны, ваше решение может отличаться)

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
        
            #определяем максимальное хп
    @property 
    def max_health_points(self) -> int:
        return self.level * self.base_health_points         #уровень * базовое хп

        #определяем % хп (здоровья)
    def health_points_percent(self):   
        return 100 * self.health_points / self.max_health_points   #хп * на максимальное хп

        #добавляем метод __str__ для информативного отображения персонажей.
    def __str__(self) -> str:
        return f"{self.character_name} (level: {self.level}, hp: {self.health_points})"



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
                #то что я добавила по заданию
        if character_1.is_alive() and not character_2.is_alive():
            if character_1.level < 3: 
                character_1.level += 1
            character_1.health_points += character_1.max_health_points / 2




        print(f" Character 1: {character_1} is_alive: {character_1.is_alive()} ")
        print(f" Character 2: {character_2} is_alive: {character_2.is_alive()}")


ork_1 = Ork(level=1)
elf_1 = Elf(level=1)

fight(character_1=ork_1, character_2=elf_1)

# 1. После убийства персонажа, уровень того, кто убил, повышается на 1.
# 2. Максимальный уровень персонажа - 3.
# 3. При повышении уровня персонажа, происходит отхил, и персонажу прибавляется половина от максимального количества хп.
# 4. Уровень должен повышаться в функции fight
# После имплементации, и запуска функции fight, при вызове должно вывестись:
# Ork is alive Ork (level: 2, hp: 140)
# Elf is dead Elf (level: 1, hp: -4)