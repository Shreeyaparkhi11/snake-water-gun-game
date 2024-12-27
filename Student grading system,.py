#initializing an empty dictionary
student = {}
#function to add student details
def add_student(stu_id):
    if stu_id not in student:
        stu_name = input("Enter student name: ").title()
        course = input("Enter the courses (seperated by commas): ").split(',')
        course = {c.strip().capitalize() for c in course}
        #storing the details in dictionry
        student[stu_id] = ({'Name': stu_name,
                            'Course': set(course),
                            'marks': {} })
        print("Student ", stu_name, " added successfully")
    elif stu_id in student:
        print("Student already exists")

#function to assign grade
def assign_marks(stu_id):
    if stu_id not in student:
        print("Error: Student ID does not exist")
    else:
        course = input("Enter the course: ").title().strip()
        if course not in student[stu_id]['Course']:
            print(f"Error: Student is not enrolled in the course '{course}'")
        else:
            marks = int(input("Enter the marks out of 100: "))
            if (marks<0) or (marks>100) :
                print("Error: Marks should be between 0 and 100")
            else:
                student[stu_id]['marks'][course] = marks
                print(f"Marks {marks} assigned successfully for {course}")

#function to display student details
def student_details(stu_id):
    if stu_id not in student:
        print('Error: Student ID does not exist')
    else:
        print("Student Details:")
        print('Name: ', student[stu_id]['Name'])
        print('Courses: ', sorted(student[stu_id]['Course']))
        print('Marks: ', student[stu_id]['marks'])

#function to display all student details
def all_student_details():
    for stu_id,i in sorted(student.items()):
        print(f'Student ID: {stu_id}')
        print(f'Name: {i["Name"]}')
        print(f'Courses: {",".join(i["Course"])}')
        print(f'Marks: {i["marks"]}')
        print('-' * 35)

#function for calculating grade
def calculate_grade(stu_id):
    if stu_id in student:
        print('The marks',student[stu_id]['Name'],'obtained in each course are: ')
        # Iterate through the marks for each student (inner dictionary)
        sum=0
        total_marks=0
        for course, marks in student[stu_id]['marks'].items():
                    print(f" {course}: {marks}")
                    sum+=marks
                    total_marks+=100   #each course is of 100 marks
        print('The total marks obtained by the student across all courses are: ',sum)
        print('The total possible marks are: ', total_marks)
        #calculating percentage
        percentage = sum / total_marks * 100
        print('The percentage obtained is: ', percentage)
        #calulating the grade
        if percentage >= 90:
            print('The grade obtained is: O')
        elif (percentage >= 80) and (percentage < 90):
            print('The grade obtained is: A+')
        elif (percentage >= 70) and (percentage < 80):
            print('The grade obtained is: A')
        elif (percentage >= 60) and (percentage < 70):
            print('The grade obtained is: B+')
        elif (percentage >= 50) and (percentage < 60):
            print('The grade obtained is: B')
        elif (percentage >= 40) and (percentage < 50):
            print('The grade obtained is: C')
        else:
            print('The grade obtained is: F')
    else:
        print('Error: Student ID does not exist')

# Function to validate student ID input
def get_valid_student_id():
    while True:
        try:
            stu_id = int(input("Enter student id: "))
            if stu_id < 0:
                print("Error: Student ID should be a positive number.")
            else:
                return stu_id
        except ValueError: 
            print("Error: Student ID should be a valid number.")

#display the menu
print("1.Add a student \n2.Assign marks \n3.View details of a student \n4.View details of all students \n5.Calculate the grades \n6.Exit the system")
print("-" * 35)

#while condition to repeat the choice input
while True:
    #input from the user for the action
    try:
        choice = int(input("Enter the number of action: "))
    except ValueError:
        print("Invalid input! \nPlease enter a number.")
        continue
    print()

    if choice == 1:
        print('Add a new student')
        add_student(get_valid_student_id())
        
    elif choice == 2:
        print('Assign marks to student')
        assign_marks(get_valid_student_id())
        more = input('Do you want to assign more marks? (y/n): ').lower()
        if more == 'n':
            break

    elif choice == 3:
        print('View student details')
        student_details(get_valid_student_id())
        
    elif choice == 4:
        print('Details of all students: ')
        all_student_details()

    elif choice == 5:
        calculate_grade(get_valid_student_id())
        
    elif choice == 6:
        ans = input('Do you want to exit the system? \nAll the data will be lost.(y/n): ').lower()
        if ans == 'n':
            continue
        else:
            print('Thank you for using the system')
            break
        
    else:
        print("invalid choice")
    print('-' * 35)
    continue
