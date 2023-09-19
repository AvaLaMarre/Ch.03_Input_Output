# This is my first program
'''
miles_driven = int(input("Enter miles driven: "))
gallons_used = int(input("Enter gallons used: "))
mpg = miles_driven/ gallons_used
print(mpg)

print("Hello! Welcome to my program")
name = input("Whats your name?: ")
print("Nice to meet you " + name)
print(" ")

print("Check out my Fahrenheit to cacl converter!")
temp = int(input("What is the temperature in Fahrenheit?"))
temp = (temp - 32) * (5 / 9)
print(temp)
print(" ")

print("Here's my area of a triangle calulator")
base = int( input("Enter a base: ") )
height= int( input("Enter a height: ") )
area = (base * height)/2
print(area)
print(" ")

print("Look at my circumference of a circle calculator")
rad= int(input("Enter a radius: "))
circum = 2 * 3.141592653589793238462643383279502884197 * rad
print(circum)
print("")

print("Input an integer and ill pop out a square root!")
int_to_squ = int( input(" Enter a integer: "))
print("")

'''

sem_grade = int(input("What is your semester grade?"))
fin_grade = int(input("What is your Final Exam grade?"))
ex_worth = int(input("What is the Final Exam worth?"))
sem_grade_worth = 100 - ex_worth
sem_grade_worth /= 100
ex_worth /= 100
overall = (sem_grade_worth * sem_grade) / (ex_worth * fin_grade)
print(overall)