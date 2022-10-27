# Домашняя задача 3. Создайте программу 
# для игры в "Крестики-нолики".

from typing import Counter


board = list(range(1, 10)) # от 1 до 9

def draw_board(board): # рисуем макет 3 х 3
    print('_' * 13) # создание границы сверху
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|') # границы с боков
        print('_' * 13) # создание границы снизу

def take_input(player_symbol): # игрок ставит символ
    valid = False
    while not valid:
        player_answer = input('Куда поставим знак ' + player_symbol + ' -> ')
        try:
            player_answer = int(player_answer)
        except:
            print('Хитрить нельзя. Вы уверены, что ввели число?')

        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in 'XO'):
                board[player_answer - 1] = player_symbol
                valid = True
            else: print('Данное поле уже занято, будь внимателен')
        else: print('ERROR. Для хода введите цифру от 1 до 9') 

def check_win(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # индексы полей
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]: # если знак в каждом поле одинаковый, возвращаем этот знак
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else: take_input('O')
        counter += 1
        if counter > 4:
            temp = check_win(board)
            if temp:
                print('Ура, выигрыш!')
                win = True
                break
        if counter == 9:
            print('Игра окончена. Ничья! В следующий раз повезет...')
            break
    draw_board(board)

main(board)
