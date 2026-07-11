class Talaba:
    def __init__(self, fname, lname, year):
        self.fname = fname
        self.lname = lname
        self.year = year
        self.course = 1

    def get_name(self):
        return self.fname

    def get_lastname(self):
        return self.lname

    def get_year(self):
        return self.year

    def get_age(self, year=2026):
        return year - self.age

    def get_info(self):
        return f"I am {self.fname} {self.lname}. I was born in {self.year}."

    def get_fullname(self):
        return f"{self.fname} {self.lname}"

    def get_course(self):
        return self.course
    
    def set_course(self, new_course):
        self.course = new_course

    def update_course(self):
        self.course += 1


class Fan:
    def __init__(self, name):
        self.name = name
        self.student_num = 0
        self.students = []

    def add_student(self, talaba):
        self.students.append(talaba)
        self.student_num += 1

    def get_name(self):
        return self.name
    
    def get_students(self):
        return [talaba.get_fullname() for talaba in self.students]
    
    def get_students_num(self):
        return self.student_num
    
talaba_1 = Talaba('javlon', 'saidov', 2005)
talaba_2 = Talaba('ali', 'valiyev', 2000)
talaba_3 = Talaba('hasan', 'husanov', 2003)
talaba_4 = Talaba('anvar', 'yoriyev', 2008)

matematika = Fan('Matematika')
fizika = Fan('Fizika')

matematika.add_student(talaba_1)
matematika.add_student(talaba_2)
matematika.add_student(talaba_3)

fizika.add_student(talaba_2)
fizika.add_student(talaba_4)


print(matematika.get_students())
print(matematika.get_students_num())


print(fizika.get_students())
print(fizika.get_students_num())