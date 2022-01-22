import random

boardpath = r'C:\Users\immun\Desktop\test\Treasure.txt'

def writeUpNumbers():
    file.write(('1' * random.randint(1,20))+('2' * random.randint(1,20))+('3' * random.randint(1,20))\
              +('4' * random.randint(1,20))+('5' * random.randint(1,20))+('6' * random.randint(1,20))\
              +('7' * random.randint(1,20))+('8' * random.randint(1,20))+('9' * random.randint(1,20)))

def writeDownNumbers():
    file.write(('9' * random.randint(1,20))+('8' * random.randint(1,20))+('7' * random.randint(1,20))\
              +('6' * random.randint(1,20))+('5' * random.randint(1,20))+('4' * random.randint(1,20))\
              +('3' * random.randint(1,20))+('2' * random.randint(1,20))+('1' * random.randint(1,20)))

def writeTreasure():
    file.write('TREASURE')

with open(boardpath,'w') as file:
    writeUpNumbers()
    writeTreasure()
    writeDownNumbers()

with open(boardpath,'r') as file:
    file.seek(0)
    choosenCell = 0
    while True:
        playerChoose = input('Where you want to move? (1 - forward, 2 - backward)\n')
        if playerChoose == '1':
            moveForward = int(input('How many characters?\n'))
            choosenCell = file.seek(choosenCell + moveForward)
            print(file.tell())
            print(choosenCell)
        elif playerChoose == '2':
            moveBackward = int(input('How many characters?\n'))
            choosenCell = file.seek(choosenCell - moveBackward)
            print(file.tell())
            print(choosenCell)
        else:
            print('Please choose 1 or 2!')






