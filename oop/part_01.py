
class Talaba:
    def __init__(self, fname, lname, year):
        self.fname = fname
        self.lname = lname
        self.year = year

    def info(self):
        return f"I am {self.fname} {self.lname}. I was born in {self.year}."
    
    def get_age(self, year = 2026):
        return year - self.year
    
    def get_name(self):
        return self.fname
    
    def get_lastname(self):
        return self.lname


talaba1 = Talaba('Javlon', 'Saidov', 2005)
talaba2 = Talaba('Ali', 'Valiyev', 2009)
talaba3 = Talaba('Hasan', 'Husanov', 1998)

print(talaba1.info())
print()
print(talaba2.get_age())
print()
print(talaba1.get_name())
print(talaba3.get_lastname())
