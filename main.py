# Function to find how much damage is dealt through armor
def calculate_damage_reduction(armor_input):
    # Calculates the effective hp as if they had 100 (Technically any number works, but 100 is easiest to understand)
    effective_hp = 100 + armor_input
    # Returns the quotient of hp (100 in this case) / effective_hp
    return 100 / effective_hp


# Function to find how much damage gets through the armor
def damage_dealt(armor_input, damage_input):
    # Finds how much percent of damage would go through using previous function
    percent_dealt = calculate_damage_reduction(armor_input)
    # Returns the percent that goes through by the damage dealt
    return damage_input * percent_dealt


# Inputs for damage_dealt function by user
damage = int(input("How much damage are you dealing?\n"))
armor = int(input("What armor would you like to test?\n"))
# Print Statement
print("Your damage dealt is " + damage_dealt(armor, damage))
