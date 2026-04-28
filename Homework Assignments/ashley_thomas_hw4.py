#Name: Tommy Ashley
#Section: A
#Description: Allow user to input and store student ID, name, and test scores into a dictionary so that an average grade per student
#             can be calculated
#
def add_student(students): #add a new student to students dictionary using user input
    student_name = input("Enter new student's name: ")
    student_id = input("Enter new student's ID: ")
    students[student_id] = {"Name": student_name} #store student name in student id key
        

def input_assignments(student, num_assignments): #input assignment grades for given student
    
    student["Scores"] = []  #create empty nested dictionary
    for i in range(0,num_assignments): #loop through number of assignments to be graded
        valid = False
        while not valid:
            score = input(f"Enter {student["Name"]}'s score for assignment {i+1}: ")
            if score.isdigit():
                valid = True
                student["Scores"].append(int(score)) #add valid assignment score to score key for given student
            else:
                print("Enter Valid Score")
        

    
def grade_student(student): #give grade for a given student
    tot = 0
    i = 0
    for score in student["Scores"]:
        tot += score
        i += 1
    student["Grade"] = tot / i  

def get_letter_grade(grade): #give a letter grade for input score
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >=70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    print()
    
def print_report(students): #print report of all students, their overall grade, letter grade, and average grade per assignment
    print("FINAL GRADE REPORTS")
    print("--------------------------------------------------------------------------------------------------------------")
    num_assignments = 0
    for student in students.values(): #loop through all students in students dictionary
        grade_student(student)
        print(f"{student["Name"]}'s average score was a {student["Grade"]:.2f}, letter grade of {get_letter_grade(student["Grade"])}")
        num_assignments = len(student["Scores"]) #keep track of num_assignments without using a global variable or another parameter
        
    print()
    print("ASSIGNMENT AVERAGES")
    print("--------------------------------------------------------------------------------------------------------------")
    

    for i in range(num_assignments): #finds average grade for every assignment
        tot = 0
        for student in students.values(): #loops through all students
            tot += student["Scores"][i] #adds up assignment score for assignment i
        avg = tot / len(students.values())
        letter = get_letter_grade(avg)
        print(f"The average for assignment {i+1} is {avg:.2f}, which is a {letter}") 
        
    
def main(): #main function
    students = {} #create an empty dictionary where all students will be stored
    add_student(students) #add first student
    
    valid = False
    while not valid: #logic to enter in as many students as user wants
        inp = input("Enter another student? (y/n): ")
        if inp == "y":
            add_student(students)
        elif inp == "n":
            valid = True
    valid = False
    while not valid:#logic for how many assignments were given
        inp = input("How many assignments were given: ")
        if inp.isdigit():
            valid = True
            num_assignments = int(inp)
        else:
            print("Invalid Input")
            
    for student in students.values(): #calls input_assignments for every student in students 
        input_assignments(student, num_assignments)
        
    print_report(students) # prints final report
        
        
    
main() #call main