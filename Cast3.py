#Coding Exercise 3.4
class Customers():
    greeting = "Welcome to the Coffee Place!"
    def __init__(self,name,beverage,food,total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.toral = total

c_1 = Customers("Samirah","Iced caffe latte", "Cinnamon roll", 225)
c_2 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)

print(Customers.greeting)
print(c_1.beverage)
print(c_2.food)

print("")
#Ending of Coding Exercise 3.4

#Coding Exercise 3.8
print(217 * 6)
print(600 + 35234)
print(67 // 12)
print(56329 % 982)
print(34 ** 5)

print("")
#Ending of Coding Exercise 3.8

#Coding Exercise 3.12
my_age = 22
mom_age = 61
sister_age = 29

print(mom_age < sister_age and my_age == 22)
print(mom_age == 61)
print(mom_age > 34 or sister_age == 22)
print(mom_age >= 54)
print(not(sister_age <= 400 and my_age == 22))

print("")
#Ending of Coding Exercise 3.12
