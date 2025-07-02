class student:
    region = 'Bucheon'

    def __init__(self, name, age, univ, gender):
        self.name = name
        self.age = age
        self.univ = univ
        self.gender = gender
        
    def print_info(self):
        print('Information of', self.name)
        print('age is', self.age)
        if (self.gender == 'M'):
            print('Gender is Male')
        else:
            print('Gender is Female')
        print(self.univ)

s1 = student('yh', 20, 'korea university', 'M')
s2 = student('km', 20, 'yonsei univeristy', 'F')

print(s2.univ)
print(s1.region)

s2.print_info()