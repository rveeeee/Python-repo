weight = int(input('Weight: '))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'L':
    converted = weight * 0.453592
    print(f"You are {converted} kilogram")
elif unit.upper() == 'K':
    converted = weight / 0.453592
    print(f"You are {converted} pounds")
else:
    print('Invalid Input')

