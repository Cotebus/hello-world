print('Enter a string:')
inputString: str = input()
subStringIndex: int = inputString.find("#")

if subStringIndex != -1:
    print(inputString[0:subStringIndex])
else:
    print(inputString)
