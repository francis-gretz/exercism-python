"""Functions for organizing and calculating student exam scores."""

MINIMUM_SCORE = 41

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    return list(map(round, student_scores))


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    return len(list(filter(lambda y: y <= 40, student_scores)))


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    return list(filter(lambda y: y >= threshold, student_scores))


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

    delta = highest - MINIMUM_SCORE
    step = round(delta / 4)
    result = []
    for index in range(4):
        result.append(MINIMUM_SCORE + index * step)

    return result


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    result = []
    for index, score in enumerate(student_scores):
        name = student_names[index]
        result.append(f"{index + 1}. {name}: {score}")
    return result


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for item in student_info:
        if len(item) > 0 and item[1] == 100:
            return item
    return []


student_info = [['Joci', 100], ['Vlad', 100],
                ['Raiana', 100], ['Alessandro', 100]]
result = perfect_score(student_info)
print(result)

student_info = [['Jill', 30], ['Paul', 73]],
result = perfect_score(student_info)
print(result)

student_info = [],
result = perfect_score(student_info)
print(result)

student_info = [['Rui', 60], ['Joci', 58], ['Sara', 91], ['Kora', 93], ['Alex', 42],
                ['Jan', 81], ['Lilliana', 40], ['John', 60], ['Bern', 28], ['Vlad', 55]],
result = perfect_score(student_info)
print(result)

student_info = [['Yoshi', 52], ['Jan', 86], ['Raiana', 100], ['Betty', 60],
                ['Joci', 100], ['Kora', 81], ['Bern', 41], ['Rose', 94]]
result = perfect_score(student_info)
print(result)
