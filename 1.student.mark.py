def InputStudent(): #input in4 of students
    students=[] #create a list
    NumberOfStudent=int(input("Enter the number of students in the class: "))
    for i in range(NumberOfStudent):
        student_name=input("Enter the %dth name: " % (i+1))
        student_id=input("Enter the student ID: ")
        student_DoB=input("Enter the DoB (Day//Month//Year): ")
        students.append({"name":student_name,"id":student_id,"DoB": student_DoB})
    return students
def InputCourse(): #input in4 of courses
    courses=[] #list too
    NumberOfCourse=int(input("Enter the number of courses: "))
    for _ in range(NumberOfCourse):
        course_name=input("Enter the course name: ")
        course_id=input("Enter the course ID: ")
        courses.append({"name":course_name,"id": course_id})
    return courses
def list_students(students): #function List students
    print("\nStudents:")
    for student in students:
        print(f"{student}")
def list_courses(courses):  #list courses
    print("\nCourses:")
    for course in courses:
        print(f"{course}")
def InputMark(students, courses): #input mark for each student in each course
    marks = {} #tuple
    for course in courses:
        course_id = course['id']
        marks[course_id] = {}
        print(f"enter the mark: {course_id}") #show ID of course
        for student in students:
            student_id = student['id'] 
            mark = float(input(f"Enter makr for {student['name']} (ID: {student_id}): "))
            marks[course_id][student_id] = mark
    return marks
def list_mark(students, courses, marks): #list mark
    for course in courses:
        course_id=course['id']
        print(f"\n{course['name']}, {(course_id)}")
        for student_id, mark in marks[course_id].items():
            student_name=next(s['name'] for s in students if s['id']== student_id) #generate name of studemt list
            print(f"{student_name},{(student_id)},: {mark}")
students=InputStudent() #like int main() code in C
courses=InputCourse()
mark=InputMark(students, courses)
list_students(students)
list_courses(courses)
list_mark(students, courses, mark)