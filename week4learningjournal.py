
def get_grade():
    grades = []
    assignment_name = ["Exam 1", "Exam 2", "Exam 3", "Homework", "Final"] # list of assignments for grades to be entered in
    for assignment in assignment_name: # creates loop, asking for grade in each assignment
        grade = int(input("What is your grade for %s? " % assignment))
        while grade < 0 or grade > 100:
            print("Grade must be a number between 0 and 100")
            grade = int(input("What is your grade for %s? " % assignment)) # asks for new input if previous was not in range
        grades.append(grade) # adds grade to list of grades
    return grades # prints out list of grades, with index 0 being Exam 1 and 4 being Final