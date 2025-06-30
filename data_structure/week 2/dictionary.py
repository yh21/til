score = {'yh' : 100, 'km' : 290, 'jh' : 200}
print(score)
score['sj'] = 300
print(score)

for student in score.keys() :
    print(student, 'student')