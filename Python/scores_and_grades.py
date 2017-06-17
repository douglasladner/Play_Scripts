#Scores and Grades
#generates random scores and displays the appropriate grade

import random

def score_grade():

    print "Scores and Grades"

    for i in range(1,10):

        score = random.randint(0,100)

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print "Score: {}; Grade: {}".format(score, grade)

    print "Done. Goodbye!"


score_grade()
