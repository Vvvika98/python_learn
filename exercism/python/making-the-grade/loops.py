"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    scores = []
    for i in student_scores:
        scores.append(round(i))
    return scores
   

# print(round_scores(student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])) 

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count = 0
    for i in student_scores:
        if i <= 40:
            print(i)
            count += 1
    return count


# print(count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]))


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best = []
    for i in student_scores:
        if i >= threshold:
            best.append(i)
            # print(i)
    return best

# print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    grades = [] #ЭТО БЫЛО СЛОЖНОЕ ЗАДАНИЕ !!!!!!!!!!!!!! Я ОБЪЯСНЕНИЕ НЕ ПОНЯЛА ВАЩЕ 
    interval = (highest - 40) // 4
    for i in range(41, highest,interval):
        grades.append(i)
    return grades
      
# print(letter_grades(highest=100)) 


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranking = []
    rank = 0
    for i, num in zip(student_names, student_scores): #функция зип для параллельной итерации по двум спискам (создавая кортеж)
        rank += 1
        ranking.append(f"{rank}. {i}: {num}")
    return ranking

# print(student_ranking(student_scores = [100, 99, 90, 84, 66, 53, 47], student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']))   


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for num in student_info:
        # print(num)
        if num[-1] == 100:
            return num
    return []


print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))