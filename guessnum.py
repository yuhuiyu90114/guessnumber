import random
start = int(input('plesase input a start number: '))
end = int(input('plesase input an end number: '))
r = random.randint(start, end)

count = 0
while True:
    user = int(input('plesase input a number between start and end: '))
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