#A simple language where all vowels in english are replaced with the letter g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))