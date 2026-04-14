def add_student(students):
    student_name = input("Enter new student's name: ")
    student_id = input("Enter new student's ID: ")
    students[student_id] = {"Name": student_name}
        

def input_assignments(student, num_assignments):
    
    student["Scores"] = [] 
    for i in range(0,num_assignments):
        valid = False
        while not valid:
            score = input(f"Enter {student["Name"]}'s score for assignment {i+1}: ")
            if score.isdigit():
                valid = True
                student["Scores"].append(int(score))
            else:
                print("Enter Valid Score")
        

    
def grade_student(student):
    tot = 0
    i = 0
    for score in student["Scores"]:
        tot += score
        i += 1
    student["Grade"] = tot / i  

def get_letter_grade(grade):
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
    
def print_report(students):
    print("FINAL GRADE REPORTS")
    print("--------------------------------------------------------------------------------------------------------------")
    num_assignments = 0
    for student in students.values():
        grade_student(student)
        print(f"{student["Name"]}'s average score was a {student["Grade"]:.2f}, letter grade of {get_letter_grade(student["Grade"])}")
        num_assignments = len(student["Scores"])
        
    print()
    print("ASSIGNMENT AVERAGES")
    print("--------------------------------------------------------------------------------------------------------------")
    

    for i in range(num_assignments):
        tot = 0
        for student in students.values():
            tot += student["Scores"][i]
        avg = tot / len(students.values())
        letter = get_letter_grade(avg)
        print(f"The average for assignment {i+1} is {avg:.2f}, which is a {letter}") 
        
    
def main():
    students = {}
    add_student(students)
    
    valid = False
    while not valid:
        inp = input("Enter another student? (y/n): ")
        if inp == "y":
            add_student(students)
        elif inp == "n":
            valid = True
    valid = False
    while not valid:
        inp = input("How many assignments were given: ")
        if inp.isdigit():
            valid = True
            num_assignments = int(inp)
        else:
            print("Invalid Input")
            
    for student in students.values():
        input_assignments(student, num_assignments)
        
    print_report(students)
        
        
    
main()