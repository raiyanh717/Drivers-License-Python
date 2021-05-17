#Drivers License Simulator

print("The system will decide if you are eligible for a probationary drivers license")

age = int(input('Enter your age: '))
score = int(input('Enter your score: '))
name = input('What is your name: ')

if age <= 16:
    print('You are too young to drive')
elif score < 80:
    print('Your score is too low, you must retake the drivers test')
else:
    print('Congratulations' + " " + name + " " + 'you are able to recieve your license')
    address = input('Enter your address: ')
    birthday = input('Enter your birthday mm/dd/yyyy: ')
    eye = input('Enter your eye color: ')
    height = input('Enter your height: ')
    gender = input('Enter your gender: ')

    for i in range(3):
        for j in range(7):
            print('x', end = '')
        print()

    print(name)
    print(address)
    print(birthday)
    print(eye)
    print(height)
    print(gender)

    for i in range(3):
        for j in range(7):
            print('x', end = '')
        print()

print('Information has been processed')
