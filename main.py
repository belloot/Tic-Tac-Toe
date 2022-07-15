board = ['-','-','-',
         '-','-','-',
         '-','-','-']

positions = {'a1':0,'a2':1,'a3':2,
             'b1':3,'b2':4,'b3':5,
             'c1':6,'c2':7,'c3':8}

GAME_DONE = False
COUNT = 0

print("Welcome!\n")

p1_name = input("Player 1's name: ")
p2_name = input("Player 2's name: ")

if p1_name.upper() == p2_name.upper():
    p2_name = p1_name + "*"
    print("\nInteresting, you guys have the same name. Player 2 will now be {}".format(p2_name))

p1_symbol = input("Player 1, pick your symbol:")
p2_symbol = input("Player 2, pick your symbol:")

CURRENT_PLAYER = p1_symbol

def show_board():
    print('\n|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

print("\nEach row is a,b,c (respectively)\nEach column is 1,2,3 (respectively)")
print("Example: Place something in the top left, type a1")
print("\nEnjoy!")

show_board()

def reset_board():
    global board

    board = ['-','-','-',
             '-','-','-',
             '-','-','-']

def check_win():
    global GAME_DONE
    #VERTICAL CHECK
    if board[0] == board[3] and board[3] == board[6]:
        if board[0] != "-":
            GAME_DONE = True
    elif board[1] == board[4] and board[4] == board[7]:
        if board[1] != "-":
            GAME_DONE = True
    elif board[2] == board[5] and board[5] == board[8]:
        if board[2] != "-":
            GAME_DONE = True
    
    #HORIZONTAL CHECK
    if board[0] == board[1] and board[1] == board[2]:
        if board[0] != "-":
            GAME_DONE = True
    elif board[3] == board[4] and board[4] == board[5]:
        if board[3] != "-":
            GAME_DONE = True
    elif board[6] == board[7] and board[7] == board[8]:
        if board[6] != "-":
            GAME_DONE = True

    #DIAGONAL CHECK
    if board[0] == board[4] and board[4] == board[8]:
        if board[0] != "-":
            GAME_DONE = True
    elif board[2] == board[4] and board[4] == board[6]:
        if board[2] != "-":
            GAME_DONE = True

def switch_turn():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == p1_symbol:
        CURRENT_PLAYER = p2_symbol
    else:
        CURRENT_PLAYER = p1_symbol

def play():
    global CURRENT_PLAYER
    global GAME_DONE
    global COUNT

    while True:
        #ENDS GAME IF TIED OR SOMEONE WINS
        if COUNT == 9:
            print("\nGame Tied! Great job {} and {}!".format(p1_name,p2_name))
            break
        elif GAME_DONE == True:
            if CURRENT_PLAYER == p1_symbol:
                print("\nCongratulations! The winner is {}".format(p1_name))
            else:
                print("\nCongratulations! The winner is {}".format(p2_name))
            break

        if CURRENT_PLAYER == p1_symbol:
            location = input("\n" + p1_name + "'s next move: ")
        else:
            location = input("\n" + p2_name + "'s next move: ")

        #PERFORMS THE PLAYER'S MOVE
        if location in positions and board[positions[location]] == '-':
            board[positions[location]] = CURRENT_PLAYER
            show_board()
            check_win()
            COUNT += 1
            if GAME_DONE == False:
                switch_turn()
        else:
            print("\nInvalid spot or spot already taken, try again.")
            continue

play()

while True:
    choice = input("\nDo you want to play again? (y/n)")

    if choice == "y":
        turn = input("\nChange who starts first? (y/n)")
        if turn == "y":
          CURRENT_PLAYER = p2_symbol
        else:
          CURRENT_PLAYER = p1_symbol
        GAME_DONE = False
        COUNT = 0
        reset_board()
        show_board()
        print("\nLet's go again!")
        play()

    elif choice == 'n':
        print("\nBye!")
        break
    else:
        print("\nInvalid input!")