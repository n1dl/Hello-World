"""name , age 18+ ."""
name = input('Enter your name: ')
age = input('How old are you? ')

message = (f'Welcome my friend, {name}!' if int(age) >= 18 else 'I\'m sorry\
    friend, this is for adults guys')

print(message)
