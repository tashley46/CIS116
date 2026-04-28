class Person():
    type = "person"
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __str__(self):
        return f"First Name: {self.first} \nLast Name: {self.last}\n"

class Student(Person):
    def __init__(self,first,last):
        super().__init__(first,last)
        self.courses = []
    def __str__(self):
        return f"Name: {self.first} {self.last} \nCourses: {self.courses}\n Type: {self.type}"
    def addCourse(self, Course):
        self.courses.append(Course)

def main():
    print("START PROGRAM")
    
    
    
    student1 = Student("Thomas", "Ashley")
    student2 = Student("John", "Doe" )
    
    for i in range(5):
        student1.addCourse(i)
        student2.addCourse(i + 2)
    
    print(student1)
    print(student2)
    
    
    
    print("END PROGRAM")
    
main()