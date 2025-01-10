#Conditional Statements
#This project used conditional statements to address different questions
#Initials
#Functions
def vote_check(): #checks if a person can vote in the US
    citizen = input("Are you a US citizen?")
    age = int(input("How old are you?"))
    if age >= 18 and citizen == Yes:
        print("You can vote!")
    else:
        print("You can't vote :(")

def max_num(a,b,c): #Prints the largest of the three numbers inputed and their value
    if a > b and a > c:
        print("a is the largest number with a value of " + str(a))
    if b > a and b > c:
        print("b is the largest number with a value of " + str(b))
    if c > b and c > a:
        print("c is the largest number with a value of " + str(c))

def score_to_grade(score): #Prints a letter grade based on the score given
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")


#Main
vote_check()
max_num(6,2,8)
score_to_grade(82)

#Boolean: True or False
#Boolean Expression: 15 > 10 A statement that evaluates to true or false

#Comparison Operators
# > greater than
# < less than
# == equal to
# >= greater than or equal to
# <= less than or equal to
# ! not equal to

#Logical Operators
# and - evaluates if both statements are true
# or - evaluates to true if one statement is true
# not - inverts the result of a boolean expression
