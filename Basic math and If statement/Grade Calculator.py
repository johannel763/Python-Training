## Asks the user for two test and one exam score
## Calculates that the exam score is at least 25/50 and then calculates the grade.

test_1 = float(input("Please enter test 1 score out of 25: "))

test_2 = float(input("Please enter test 2 score out of 25: "))

final_exam = float(input("Please enter exam score out of 50: "))

final_score = (test_1 + test_2 + final_exam) / 100 * 100

if final_exam < 25:
    print("Fail")

if final_score > 80:
    print("Distinction")
elif final_score < 80 and final_score > 60:
    print("Credit")
elif final_score < 60:
    print("Pass")