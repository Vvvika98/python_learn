"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, Dexercism download --track=python --exercise=plane-tickets

    """

    character = "ABCD"
    for i in range(number):
        # print(i)   #0,1,2,3
        yield character[i%len(character)]   #character[0] = A, character[1] = B...  


letters = generate_seat_letters(4)
# print(next(letters))
# print(next(letters))



def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    row = 0   #ряд
    
    for i, seat in enumerate(generate_seat_letters(number)):  #generate_seat_letters(number)
        # print(i,seat)    #0 A, 1 B, 2 C, 3 D.... 
        if i % 4 == 0:   #если i без остатка делиться на 4, 
            row += 1     #начинаем новый ряд 
        if row == 13:    #ЕСЛИ РЯД 13 
            row += 1     
        yield f"{row}{seat}"  
    

seats = generate_seats(56)

# for _ in range(56):
#     print(next(seats))

# print(next(seats))




def assign_seats(passengers):    #Ваня сказал переписать, используя dict_comt + zip
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    result = {}    #пустой словарь
    places = generate_seats(len(passengers))  #места - общее кол-во = кол-ву пассажиров
    for passenger in passengers:     #вычленяем пассажиров по одному
        result[passenger] = next(places)  #добавляем в словарь пары ключ=значение, используя генератор функции выше!

    return result

passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']
# print(assign_seats(passengers))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for num in seat_numbers:
        # yield ((str(num)+ flight_id).ljust(12, "0"))
        yield f"{num}{flight_id}".ljust(12,"0")
        


seat_numbers = ['1A', '17D']
flight_id = 'CO1234'
ticket_ids = generate_codes(seat_numbers, flight_id)    

# print(next(ticket_ids))
# print(next(ticket_ids))