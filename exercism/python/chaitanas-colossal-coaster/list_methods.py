"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    if ticket_type:  #можно не писать 1
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue

# print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"))
# print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"))

def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    
    return queue.index(friend_name)

# print(find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve"))    


def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue

    
# print(add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky"))

def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """

    queue.remove(person_name)
    return queue

# print(remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"))


def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """

    return queue.count(person_name)
    
# print(how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"))

def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

    return queue.pop()

# print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))

def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    # new_queue = queue.copy() #создать копию, для того, чтобы сохранить исходный список
    # new_queue.sort()
    # return new_queue 

    return sorted(queue) #если используем копию то лучше пользоваться функцией, а если изменить список - методом 
    
# print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))
