protagonist = "Uchiha Sasuke"

# Check if all characters are uppercase
print(protagonist.isupper())

# Return length of string
print(len(protagonist)) 

# Retrieve character from string. P.S indexing starts at 0
print(protagonist[0])

# Find the location of a specific character or sub-string. If parameter is a sub-string, it returns the location where the string starts 
print(protagonist.index("S"))
print(protagonist.index("Sasuke"))

#Replacing a part of the string
print(protagonist.replace("Sasuke","Sarada"))

