"""Solution to Ellen's Alien Game exercise."""



class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int

    x_coordinate: int - Position on the x-axis.
    
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0   #счетчик

    def __init__(self, x, y):   #создаем класс и инициализируем у него атрибуты (координаты х и у)
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1


    #метод класса (урон)
    def hit(self):
        if self.health >= 0:
            self.health -= 1
        if self.health < 0:
            self.health = 0
        

    #метод проверки жив ли пришелец
    def is_alive(self):
        return self.health > 0

    #метод телепорт, меняющий координаты
    def teleport(self, a, b):
        self.x_coordinate = a
        self.y_coordinate = b
        return self.x_coordinate, self.y_coordinate

    #метод определения обнаружения столкновений (с заглушкой)
    def collision_detection(self, other_object):
        pass


alien = Alien(2, 0) #создаем объект класса с передачей агуметентов  
    # проверка 1(доступ к атрибутам класса)
print(alien.x_coordinate)
print(alien.y_coordinate)
print(alien.health)
    

alien.hit()    #вызываем метод для получения урона

    #проверка 2(доступ к атрибутам класса)
print(alien.health)

    # проверка 3
    #уменьшем методом здоровье, проверяем новый метод
alien.hit()
print(alien.health)
print(alien.is_alive())
    
    #еще раз уменьшем методом здороьве теперь оно = 0, пришелец мертв
alien.hit()
print(alien.health)
print(alien.is_alive())

    # проверка 4
alien.teleport(5, -4)
print(alien.x_coordinate)
print(alien.y_coordinate)

    # проверка 5
# print(alien.collision_detection(other_object))
alien_2 = Alien(3,7)

    # проверка 6
alien2 = Alien(1,3)
print(Alien.total_aliens_created)

#7 
def new_aliens_collection(alien_start_positions):
    aliens = []
    for x,y in alien_start_positions:
        print()
        alien = Alien(x,y)
        aliens.append(alien)
    return aliens


    
alien_start_positions = [(4, 7), (-1, 0)]
aliens = new_aliens_collection(alien_start_positions)

for alien in aliens:
    print(alien.x_coordinate, alien.y_coordinate)



