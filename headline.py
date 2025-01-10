#Headline Generator
#Initial

#Functions
def believe_headline():
    noun = input("Please enter a noun:")
    pPronoun = input("Please enter a possesive pronoun (His/Her/Their):")
    place = input("Please enter a place:")
    print("You won't believe what this " + noun + " found in " + pPronoun + " " + place + "!")

def industry_headline():
    pluralNoun = input("Please enter a plural noun:")
    verb = input("Please enter an -ing verb:")
    noun = input("Please enter a noun:")
    print("Are " + pluralNoun + " " + verb + " the " + noun + " industry?")

def secrets_headline():
    name = input("Please enter a name")
    number = input("Please enter a number")
    Ppronoun = input("Please enter a personal pronoun (Him/Her/Them)")
    pronoun = input("Please enter a pronoun (His/Her/Their)")
    print(name + " reveals " + Ppronoun + " secrets! " + "(" + str(number) + " facts you never knew about " + pronoun + ")" )
#Main
believe_headline()
industry_headline()
secrets_headline()
