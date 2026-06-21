class student_managment:
    rollno = 1

    def __init__(self):
        self.rollno = 1
        self.student = []
        self.menu()

    def menu(self):
        user_input = input("""
        Welcom to you
        1.Add student
        2.View All Student
        3.Search Student
        4.Show Topper
        5.exit
            """)

        if user_input == '1':
            self.add_student()
        elif  user_input == '2':
            self.view_All_students()
        elif  user_input == '3':
            self.search_student()
        elif  user_input == '4':
            self.Show_Topper()
        
        elif  user_input == '5':
            exit()

    def add_student(self):
        
        print(f"Rollno = {self.rollno}")
        sdt_name = input("enter your Name:")

        sdt_age = int(input("enter your Age:"))

        sdt_marks = int(input("enter your marks:"))

        if sdt_age < 21 and sdt_marks < 500:
            student = {
            "rollno":self.rollno,
            "Name": sdt_name,
            "Age": sdt_age,
            "marks": sdt_marks
        }
            self.student.append(student)
            print("succesfully added  student....")
            self.rollno += 1
        else:
            print("Invalid document..")
        self.menu()
    
    def view_All_students(self):
        print(self.student,sep = "   ")
        self.menu()

    def search_student(self):
        sdt_roll = int(input("enter your rollno:"))
        for student in self.student:

            if student['rollno'] == sdt_roll :
                print("searching.......")
                print('Student Found')
                print("Rollno:",student['rollno'] )
                print("Name:",student['Name'] )
                print("Age:",student['Age'] )
                print("Marks:",student['marks'] )
                return
            else:
                print("Student Not found")
        self.menu()

    def Show_Topper(self):
        if len(self.student) == 0:
            print("No Student found")
            return
        
        Topper = self.student[0]

        for student in self.student:
            if student["marks"] > Topper["marks"]:
                Topper = student
            print("\n===Topper===")
            print("Rollno:",Topper['rollno'] )
            print("Name:",Topper['Name'] )
            print("Age:",Topper['Age'] )
            print("Marks:",Topper['marks'] )
            return
        self.menu()       







a = student_managment()
