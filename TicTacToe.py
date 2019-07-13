import random
from IPython.display import clear_output


choice_to_position={'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8}

def display_tictaktoe(lst):
    clear_output()
    print("    |   | ")
    print("  {} | {} | {}".format(lst[6],lst[7],lst[8]))
    print("    |   | ")
    print("------------")
    print("    |   | ")
    print("  {} | {} | {}".format(lst[3],lst[4],lst[5]))
    print("    |   | ")
    print("------------")
    print("    |   | ")
    print("  {} | {} | {}".format(lst[0],lst[1],lst[2]))
    print("    |   | ")

def check_win(board,marker):
    mark_index=[]
    win_combination={'c1':[0,1,2],'c2':[3,4,5],'c3':[6,7,8],'c4':[0,3,6],
                     'c5':[1,4,7],'c6':[2,5,8],'c7':[0,4,8],'c8':[2,4,6]}
    for num in range(0,len(board)):
        if board[num]== marker:
            mark_index.append(num)
    #print(mark_index)
    #print(mark_index in win_combination.values())
    for a_win_comb in win_combination.values():
        #print("Printing a_win_comb {}".format(a_win_comb))
        #print(a_win_comb in mark_index)
        if all(elem in mark_index  for elem in a_win_comb) and len(mark_index) >=3:
            return True
    else:
        return False

def player_choice(board):
    check_input=True

    while check_input:

        choice = int(input("Choose your next postion:(1-9)"))
        check_input=check_invalid(board,choice)


    return choice-1

def check_invalid(board, choice):
    if choice in range (1,10):
            position=choice_to_position[str(choice)]

            if check_space(board,position):
                return False
            else:
                print("The postion {} is already occupied. Please choose another position.".format(choice))
                return True
    else:
        return True



def check_space(board,position):

    if board[position]!='X'and board[position]!='O':
        return True
    else:
        return False

def check_full_space(board):

    for mark in board:
        #print(mark)
        if mark != 'X' and mark !='O':
            return False
    else:
        return True
def edit_board(board,marker,position):
    board[position]=marker
    display_tictaktoe(board)
def choose_first():
    return random.randint(1,2)
def replay():
    again= input("Do you want to play again ? Yes/No : ")
    if again.lower()=='yes':
        return True
    else:
        return False
def start_game():


    again=True


   # print("This is outside the if")
    #print("Player {} going 1st ".format(first_player))

    while again:
        print("Welcome to the Tic Tac Toe")
        print()
        print()
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_tictaktoe(board)
        marker_list=['X','O']
        players={'1':['Player 1',''], '2':['Player 2','']}
        end_game=False;
        second_player=''


        first_player=str(choose_first())
        if first_player == '1':
            second_player='2'
            #second_player_name = players['2'][0]
            print("Player {} going 1st ".format(players['1'][0]))
            players['1'][1]= input("Player 1 choose your marker. (X or O):")
            marker_list.pop(marker_list.index( players['1'][1]))
            players['2'][1]=marker_list[0]
        else:
            second_player='1'
            #second_player_name=players['1'][0]
            print("Player {} going 1st ".format(players['2'][0]))
            players['2'][1]= input("Player 2 choose your marker. (X or O):")
            marker_list.pop(marker_list.index(players['2'][1]))
            players['1'][1]=marker_list[0]


        while not end_game :
            #print(check_full_space(board))
            print("{}'s turn".format(players[first_player][0]))
            choice=player_choice(board)
            board[choice]=players[first_player][1]
            display_tictaktoe(board)
            print(board)
            print("The marker of {} is {}".format(players[first_player][0],players[first_player][1]))
            end_game=check_win(board,players[first_player][1])
            if end_game:
                print("{}!!! has won the game.".format(players[first_player][0]))
                break
            else:
                if check_full_space(board):
                    print("The game is a draw")
                    break

            print("{}'s turn".format(players[second_player][0]))
            choice=player_choice(board)
            board[choice]=players[second_player][1]
            display_tictaktoe(board)
            print(board)
            print("The marker of {} is {}".format(players[second_player][0],players[second_player][1]))
            end_game=check_win(board,players[second_player][1])
            if end_game:
                print("{}!!! has won the game.".format(players[second_player][0]))
                break
            else:
                if check_full_space(board):
                    print("The game is a draw")
                    break

        if not replay():
            print("Goodbye. Thank you for playing.")
            break

start_game()
