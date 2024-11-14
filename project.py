'''
Project Name: Rock, Paper and Scissors
Description: this program is a simple, yet detailed, implementation of the famous game Rock, Paper and Scissors
'''
from time import sleep
from random import choice

def input_validation() -> int:
    while True:
        try:
            n = int(input('Insert the amount of matches or hands per match : '))
            if(n > 0):
                return n
            else:
                print('The amount must be greater than 0!')
        except ValueError:
            print('The amount must be an integer greater than 0!')

class Player():
    _symbols = ('Rock', 'Scissors', 'Papers')    

    def __init__(self, name):
        self.name = name    
        self.__win = 0
        self.__loss = 0
        self.__ties = 0
    def get_win(self) -> int:
        return self.__win
    def get_loss(self) -> int:
        return self.__loss
    def get_ties(self) -> int:
        return self.__ties
    def get_symbol(self) -> str:
        return choice(Player._symbols)
    def increment_win(self) -> None:
        self.__win += 1
    def increment_loss(self) -> None:
        self.__loss += 1
    def increment_ties(self) -> None:
        self.__ties += 1
    def __str__(self) -> str:
        return 'Player : ' + self.name + " Win : " + str(self.__win) + " Loss : " + str(self.__loss) + " Ties: " + str(self.__ties) + "\n"

def get_hand_winner(symbol1: str, symbol2: str) -> int: 
    if( (symbol1 == Player._symbols[0] and symbol2 == Player._symbols[1]) or
        (symbol1 == Player._symbols[1] and symbol2 == Player._symbols[2]) or
        (symbol1 == Player._symbols[2] and symbol2 == Player._symbols[0])):
        return 1
    elif ( (symbol2 == Player._symbols[0] and symbol1 == Player._symbols[1]) or
            (symbol2 == Player._symbols[1] and symbol1 == Player._symbols[2]) or
            (symbol2 == Player._symbols[2] and symbol1 == Player._symbols[0])):
        return -1
    else:
        return 0

matches_amount = input_validation()

print('The match is about to start...')
sleep(3)
print('Match is starting!')

first_player = Player(input("Insert the name of the first player : "))
second_player = Player(input('Insert the name of the second player : '))

for i in range(matches_amount):
    hands_amount = input_validation()

    first_player_hands_won = 0
    second_player_hands_won = 0

    for j in range(hands_amount):
        first_player_symbol = first_player.get_symbol()
        second_player_symbol = second_player.get_symbol()

        hand_result = get_hand_winner(first_player_symbol, second_player_symbol)

        if(hand_result == 1):
            first_player_hands_won += 1
        elif(hand_result == -1):
            second_player_hands_won += 1
    if(first_player_hands_won > second_player_hands_won):
        first_player.increment_win()
        second_player.increment_loss()
    elif(second_player_hands_won > first_player_hands_won):
        second_player.increment_win()
        first_player.increment_loss()
    else:
        first_player.increment_ties()
        second_player.increment_ties()
print("The matches are over!\n Following, the scores of the two players : " + str(first_player) + "\n" + str(second_player))

  





