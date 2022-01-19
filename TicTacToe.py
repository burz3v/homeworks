#Tic Tac Toe

print('Welcome to Tic Tac Toe Game!')

#board
board = [['_','_','_'],['_','_','_'],['_','_','_']]

#function that draws the board
def drawBoard():
    print('-' * 10)
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + '     1.1 | 1.2 | 1.3')
    print(board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + '     2.1 | 2.2 | 2.3')
    print(board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + '     3.1 | 3.2 | 3.3')
    print('-' * 10)                         #the 1.1,2.2 matrix only for a player comfort

#turn of X player
def xTurn():
    valid = False
    while not valid:
        player_answer1 = input('Please choose a string: ')
        player_answer1 = int(player_answer1) - 1
        if player_answer1 >= 0 and player_answer1 < 3:  #cheking if player choosed correct number
            player_answer2 = input('Please choose a column: ')
            player_answer2 = int(player_answer2) - 1
            if player_answer2 >= 0 and player_answer2 < 3:
                if str(board[player_answer1][player_answer2]) not in 'XO':
                    board[player_answer1][player_answer2] = 'X'
                    valid = True
                else:
                    print('The cell is already choosen, take anoter!')
        else:
            print('Please write a number from 1 to 3')

#turn of O player
def oTurn():
    valid = False
    while not valid:
        player_answer1 = input('Please choose a string: ')
        player_answer1 = int(player_answer1) - 1
        if player_answer1 >= 0 and player_answer1 < 3:
            player_answer2 = input('Please choose a column: ')
            player_answer2 = int(player_answer2) - 1
            if player_answer2 >= 0 and player_answer2 < 3:
                if str(board[player_answer1][player_answer2]) not in 'XO':
                    board[player_answer1][player_answer2] = 'O'
                    valid = True
                else:
                    print('The cell is already choosen, take anoter!')
        else:
            print('Please write a number from 1 to 3')

#function checks who win
def checkWin():
    for i in board:
        if board[0][0] == board[0][1] == board[0][2] in 'X':
            win = True
            return win
        elif board[1][0] == board[1][1] == board[1][2] in 'X':
            win = True
            return win
        elif board[2][0] == board[2][1] == board[2][2] in 'X':
            win = True
            return win
        elif board[0][0] == board[1][0] == board[2][0] in 'X':
            win = True
            return win
        elif board[0][1] == board[1][1] == board[2][1] in 'X':
            win = True
            return win
        elif board[0][2] == board[1][2] == board[2][2] in 'X':
            win = True
            return win
        elif board[0][0] == board[1][0] == board[2][0] in 'O':
            win = True
            return win
        elif board[0][1] == board[1][1] == board[2][1] in 'O':
            win = True
            return win
        elif board[0][2] == board[1][2] == board[2][2] in 'O':
            win = True
            return win
        elif board[0][0] == board[0][1] == board[0][2] in 'O':
            win = True
            return win
        elif board[1][0] == board[1][1] == board[1][2] in 'O':
            win = True
            return win
        elif board[2][0] == board[2][1] == board[2][2] in 'O':
            win = True
            return win
        elif board[0][0] == board[1][1] == board[2][2] in 'X':
            win = True
            return win
        elif board[0][0] == board[1][1] == board[2][2] in 'O':
            win = True
            return win
        elif board[0][2] == board[1][1] == board[2][0] in 'X':
            win = True
            return win
        elif board[0][2] == board[1][1] == board[2][0] in 'O':
            win = True
            return win
        else:
            win = False
            return win

#main game function
def game():
    counter = 0
    while checkWin() == False:
        drawBoard()
        if counter % 2 == 0:
            xTurn()
        else:
            oTurn()
        counter += 1
        checkWin()
        if counter == 9:                #if no one wins till 9 move, it's a draw
            print(drawBoard())
            print('DRAW')
            break
        elif checkWin() == False:
            continue
        else:
            print(drawBoard())
            print('We have a winner!')
            break

game()




'''
board = list(range(1,10))
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)'''