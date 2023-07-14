a = "3"
b = "4"
print(a + b) #031

print("HI" * 3) #032

print("-" * 80) #033

t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4) #034

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : %s 나이 : %d" % (name2, age2)) #035

print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2)) #036

print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}") #037

상장주식수 = "5,969,782,550"
상장주식수_1 = 상장주식수.replace(",", "")
상장주식수_2 = int(상장주식수_1)
print(type(상장주식수_2)) #038

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7]) #039

data = "   삼성전자    "
data_1 = data.split()
print(data_1) #040