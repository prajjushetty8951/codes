string = input()
upper_case_letter = ""

for character in string:
    is_upper = (character == character.upper())
    if is_upper:
        upper_case_letter = upper_case_letter + character
print(upper_case_letter)