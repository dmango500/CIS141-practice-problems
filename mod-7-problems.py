'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(input):
    count = 0
    vowels = "aeiou"
    for letters in input:
        if letters in vowels:
            count += 1
    return count
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palindrome(s):
    reversed_s = s[::-1]
    return s.lower() == reversed_s.lower()

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        print("Super Effective")
    elif attacker == "Fire" and defender == "Water":
        print("Not very Effective")
    elif attacker == "Electric" and defender == "Grass":
        print("Neutral")

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    farecount = 0
    if 19 <= age <= 64:
        if vehicle == "yes":
            farecount += 20
        else:
            farecount += 10
    if age >= 65:
        if vehicle == "yes":
            farecount += 15
        else:
            farecount += 5
    if 0 <= age <= 18:
        farecount = 0
    return farecount
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
def level_up(experience):
    if 0 <= experience <= 99:
        return print("Level 1")
    if 100 <= experience <= 199:
        return print("Level 2")
    if experience >= 200:
        return print("Level 3")


