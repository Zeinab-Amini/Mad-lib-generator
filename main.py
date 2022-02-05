import random

contry = input("Choose a contry: ")
adverb = input("Choose an adverb: ")
print(f"If you are travling in {contry} and find yourself having to cross a piranha-filled river, here's how to do it {adverb}. ")

def print_1(adjective):
    print(f"Piranhas are more {adjective} during the day, so cross the river at night. ")
def print_2 (animal, verbing, verb):
    print(f"Avoid areas with netted {animal} traps-piranhas may be {verbing} there looking to {verb} them! ")
def print_3 (verbing, adverb, adjective):
    print(f"When {verbing} the river, swim {adverb} . You don't want to wake them up and make them {adjective}!")
def print_4 (place, liquid, body_part, verb):
    print(f"Whatever you do, if you have an open wound, try to find another way to get back to the {place}. Piranhas are attracted to fresh {liquid} and will most likely take a bite out of your {body_part} if you {verb} in the water!")

how = random.randint(1,4)
if how == 1:
    adjective = input("Choose an adjective: ")
    print_1(adjective)
elif how == 2:
    animal = input("Choose an animal: ")
    verbing = input("Choose a verb ending with 'ing': ") 
    verb = input("Choose a verb: ")
    print_2(animal, verbing, verb)
elif how ==3:
    verbing = input("Choose a verb ending with 'ing': ")
    adverb =  input("Choose an adverb: ")
    adjective = input("Choose an adjective: ")
    print_3(verbing, adverb, adjective)
else:
    place = input("Choose a place: ")
    liquid = input("Choose a liquid: ")
    body_part= input("Choose a body part: ")
    verb = input("Choose a verb: ")
    print_4(place, liquid, body_part, verb)