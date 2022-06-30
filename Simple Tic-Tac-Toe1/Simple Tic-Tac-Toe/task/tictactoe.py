start = list('_________')
board = [[start[0], start[1], start[2]],
         [start[3], start[4], start[5]],
         [start[6], start[7], start[8]]]
count = 0

def display():
    print('---------')
    print('| {} {} {} |'.format(board[0][0], board[0][1], board[0][2]))
    print('| {} {} {} |'.format(board[1][0], board[1][1], board[1][2]))
    print('| {} {} {} |'.format(board[2][0], board[2][1], board[2][2]))
    print('---------')


def win():
    _result = ''
    for i in board:
        if len(set(i)) == 1:
            _result = i[0] + ' wins'
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            _result = board[0][j] + ' wins'
    if board[0][0] == board[1][1] == board[2][2]:
        _result = board[0][0] + ' wins'
    if board[0][2] == board[1][1] == board[2][0]:
        _result = board[0][2] + ' wins'
    if _result == '':
        _result = 'Draw'
    # if _result not in ['X wins', 'O wins', 'Draw']:
    #     return 'Impossible'
    return _result


def check_input(turn):
    global board
    global start
    global count
    x, y = input().split(' ')
    while True:
        try:
            x = int(x) - 1
            y = int(y) - 1
            if x not in range(0, 3) or y not in range(0, 3):
                print('Coordinates should be from 1 to 3!')
                x, y = input().split(' ')
                continue
            if board[x][y] in ['X', 'O']:
                print('This cell is occupied! Choose another one')
                x, y = input().split(' ')
                continue
            board[x][y] = turn
            count += 1
            break
        except ValueError:
            print('You should enter numbers!')
            x, y = input().split(' ')
            continue


def progress():
    if win() in ['X wins','O wins']:
        print(win())
        return True
    if count == 9:
        print('Draw')
        return True

def main():
    while True:
        display()
        check_input('X')
        display()
        if progress(): break
        check_input('O')
        display()
        if progress(): break


main()