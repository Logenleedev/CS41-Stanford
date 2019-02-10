import sys
'''

class StanfordCourse:
    def __init__(self, department, code, title):
        self.department = department
        self.code = code
        self.title = title
# p = StanfordCourse("CS","Python","Intro to python")

class StanfordCSCourse(StanfordCourse):
    def __init__(self, department, code, title, recorded=False):
        super().__init__(department, code, title)# or StanfordCourse.__init__(self,department, code, title)
        self.is_recorded = recorded
a = StanfordCourse("CS", "106A", "Programming Methodology")

b = StanfordCSCourse("CS", "106B", "Programming Abstractions")
x = StanfordCSCourse("CS", "106X", "Programming Abstractions", recorded=True)


# print(a.code)  # => "106A"
# print(b.code)  # => "106B"



# type(a)
# print(isinstance(a, StanfordCourse))
# print (isinstance(b, StanfordCourse))
# print(isinstance(x, StanfordCourse))
# print(isinstance(x, StanfordCSCourse))
# # print(issubclass(x, StanfordCSCourse))
# print(issubclass(StanfordCSCourse, StanfordCourse))   ****************
# print(type(a) == type(b))
# print(type(b) == type(x))
# print(a == b)
# print(b == x)

'''


class StanfordCourse:
    def __init__(self, department, code, title):
        self.department = department
        self.code = code
        self.title = title
        
    def mark_attendance(self, *students):
        self.students = students
        for n in students:
            print(n,"is here ")

    
    def is_present(self, student):
        self.student = student
        if self.student in self.students:
            return True
        else:
            return False


class StanfordCSCourse(StanfordCourse):
    def __init__(self, department, code, title, recorded=False):
        super().__init__(department, code, title)# or StanfordCourse.__init__(self,department, code, title)
        self.is_recorded = recorded

p = StanfordCSCourse("CS","41","Computer Science")

p.mark_attendance("James","Rieder","Allen","Grace")
print(p.is_present("James"))

# Case (A)
try:
    print("Try")
    raise Exception('An on-purpose exception.')
except Exception as exc:
    print(exc)
else:
    print("Else")
finally:
    print("Finally")

