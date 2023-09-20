# This is my first program
'''
print("Hello! Welcome to my program")
name = input("Whats your name?: ")
print("Nice to meet you " + name)
print(" ")

print("Here's my area of a triangle calculator")
base = int(input("Enter a base: "))
height = int(input("Enter a height: "))
area = (base * height)/2
print(area)
print(" ")

print("Look at my circumference of a circle calculator")
rad = int(input("Enter a radius: "))
circum = 2 * 3.141592653589793238462643383279502884197 * rad
print(circum)
print(" ")
'''
print("Input an integer and ill pop out a square root!")
int_to_squ = int(input(" Enter a integer: "))
int_to_squ =
print("")

print("May the mass times acceleration be with you!")
mass = int(input("What is the mass?: "))
acc = int(input("What is the acceleration?: "))
force = mass * acc
print("The force is", + force)
print("Get it?")
print("")

print("Check out my Fahrenheit to calculator converter!")
temp = int(input("What is the temperature in Fahrenheit?"))
temp = (temp - 32) * (5 / 9)
print(temp)
print(" ")

trap_b1 = int(input("What is the first base?: "))
trap_b2 = int(input("What is the second base?: "))
trap_h = int(input("What is the height?: "))
trap_area = ((trap_b1 + trap_b2)/2) * trap_h
print(trap_area)
print("")

sem_grade = int(input("What is your semester grade?"))
fin_grade = int(input("What is your Final Exam grade?"))
ex_worth = int(input("What is the Final Exam worth?"))
sem_grade_worth = 100 - ex_worth
sem_grade_worth /= 100
ex_worth /= 100
overall = (sem_grade_worth * sem_grade) + (ex_worth * fin_grade)
print(overall)
