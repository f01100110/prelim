def letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 75:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
    
def pass_or_fail(grade):
    if grade >= 75:
        return 'Passed'
    else:
        return 'Failed'

def save_student_record(first_name, last_name, grade , letter_grade, pass_or_fail):
    with open('D:\\edp_f01100110\\grades.txt', 'a') as file:
        file.write(f"First Name: {first_name} | Last Name: {last_name} | Grade: {grade} | Letter Grade: {letter_grade} | Result: {pass_or_fail}\n")

while True:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    grade = int(input("Enter your grade: "))
    letter_grade = letter_grade(grade)
    pass_or_fail = pass_or_fail(grade)
    
    print(f"Your letter grade is: {letter_grade}")
    print(f"You have {pass_or_fail}.")

    save_student_record(first_name, last_name, grade, letter_grade, pass_or_fail)
    print("Record saved successfully!\n")

    choice = input("Do you want to add another student? (yes/no): ").lower()
    if choice != "yes":
        print("All students have been added. Exiting the program.")
        break