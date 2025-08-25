class student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

s1 = student('yh', 20, 4.5)
s2 = student('km', 20, 3.5)

print(s1.name)

s2.clocking = True
if s2.clocking == True:
    print('{} is clocking'.format(s2.name))