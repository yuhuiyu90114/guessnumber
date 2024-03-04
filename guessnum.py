import random
r = random.randint(1, 100)
count = 0
while True:
    user = int(input('plesase input a number between 1 and 100: '))
    count += 1
    if user == r:
        print('you are right!')
        print('it is ', count, 'time')
        break
    elif user > r:
        print('your number is bigger than answer.')
    elif user < r:
        print('your number is smaller than answer.')
    print('it is ', count, 'time')