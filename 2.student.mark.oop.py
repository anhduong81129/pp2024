class Student: #object student
    def __init__(self, student_name, student_id, DoB):
        self.student_name = student_name
        self.student_id = student_id
        self.DoB = DoB
        self.mark={}
    def enter_mark(self,course_id, mark):
        self.mark[course_id] = mark
    def list_marks(self, course_id, course_name):
        mark = self.mark.get(course_id,"No mark input")
        return f"{self.student_name}\n{course_name}: {mark}"
    def __str__(self):
        return f"Student name: {self.student_name}, Student ID: {self.student_id}, DoB: {self.DoB}"

class Course: #object course
    def __initialize__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
    def __str__(self):
        return f"Course name: {self.course_id}, Course ID: {self.course_id}"

class List_Info: #object list info
    def __initialize__(self):
        self.students=[]
        self.courses=[]
    def add_student(self, number_of_students): #add student
        for _ in range(number_of_students):
            student_name= input("Enter student name:")
            student_id= input("Enter student ID: ")
            DoB= input("Enter the student DoB: ")
            student = Student(student_name, student_id, DoB)
            self.students.append(student)
    def add_course(self, number_of_courses): #add course
        for _ in range(number_of_courses):
            course_name= input("Enter the course name: ")
            course_id= input("Enter the course ID: ")
            course= Course(course_name, course_id)
            self.courses.append(course)
    def enter_mark(self): #enter mark for student
        for student in self.students:
            print(f"Enter the mark for {student.student_name}: ")
            for course in self.courses:
                try:
                    mark = float(input(f"Enter mark for {course.course_name}: "))
                    student.enter_mark(course.course_id, mark)
                except ValueError:
                    print("Invalid mark. Please enter a numeric value.")
    def display_students(self): #show list of students
        print("Students List: ")
        for student in self.students:
            print(student)
    def display_courses(self): #same with courses
        for course in self.courses:
            print(course)
    def display_marks(self): #show marks
        student_id = input("Enter student ID: ")
        course_id = input("Enter the course ID: ")
        student = next((s for s in self.students if s.student_id == student_id), None) #enter mark for each student and course
        if student:
            course = next((c for c in self.courses if c.course_id == course_id), None)
            if course:
                print(student.list_marks(course.course_id, course.course_name)) #show mark for each course
            else:
                print("That course does not exist!")
        else:
            print("That student does not exist!")
    def main(self): #main func
            number_of_students= int(input("Enter the number of students: "))
            self.add_student(number_of_students)
            number_of_courses= int(input("Enter the number of courses: "))
            self.add_course(number_of_courses)
            self.enter_mark()
            while True:   #switch case in C
                print("\nChoose an option: ")
                print("1. Display list of students")
                print("2. Display list of courses")
                print("3. Display marks of a student:")
                print("4. Exit")

                choice = input("Enter choice: ")
                if choice == '1':
                    self.display_students()
                elif choice == '2':
                    self.display_courses()
                elif choice == '3':
                    self.display_marks()
                elif choice == '4':
                    break
                else:
                    print("NOT exist choice! ")

if __name__=="__main__": #private of main func
    list_info= List_Info()
    list_info.main()