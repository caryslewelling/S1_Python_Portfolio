#Carys Lewelling
#10/17/24

print("Welcome to the fall character 400")
print("Answer these questions to find out what fall thing you are!")
ans = input("Autumn (a) or Fall (f)?")
if ans == "a":
    ans = input("Trick (tri) or Treat (tre)?")
    if ans == "tri":
        ans = input("Orange (o) or Yellow (y)?")
        if ans == "o":
            print("You are a pumpkin!")
        else:
            print("You are a Jack O Lantern!")
    if ans == "tre":
        ans = input ("Football (fb) or Movies (m)?")
        if ans == "fb":
            print("You are pumpkin pie!")
        else:
            print("You are apple pie!")

if ans == "f":
    ans = input("Thanksgiving (t) or Halloween (h)?")
    if ans == "t":
        ans = input("Turkey (tk) or Mashed Potatoes (mp)?")
        if ans == "tk":
            print("You are a bat!")
        else:
            print("You are a black cat!")
    if ans == "h":
        ans = input("Spooky (s) or Haunted (ht)?")
        if ans == "s":
            print("You are a Witch!")
        else:
            print("You are a Ghost!")

print("Thank you for playing fall character 400!")
