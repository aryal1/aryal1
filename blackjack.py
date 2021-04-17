import random

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# class imitating player's hand, it contains some cards and their summed value, and simple options
class Hand:

    def __init__(self, function):

        self.cards_in_hand = []
        self.aces = 0
        self.values = 0
        self.function = function


    def adjust_for_ace(self):

        if self.aces > 0:
            if self.values > 21:
                self.values -= 10
                self.aces -= 1


    def hit(self, new_card):

        self.cards_in_hand.append(new_card)

        self.values += new_card.value

        if new_card.rank == 'ace':
            self.aces += 1

    def display_cards(self):

        print(f"{self.function.upper()}'S CARDS:")
        for i in self.cards_in_hand:
            print(i)


    def dealer_card(self):

        print(f"DEALER'S CARD: {self.cards_in_hand[0]}")

    def display_given_card(self):

        print(f"{self.function.upper()} HITS: {self.cards_in_hand[-1]}")

    def put_cards_away(self):

        del self.cards_in_hand[:]
        self.values = 0

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_card(self):

        return self.all_cards.pop()


class Chip:

    def __init__(self):

        self.total = 100
        self.bet = 0

    def give_chips(self):

        self.total += self.bet*2

    def deposit_chips(self):

        self.total -= self.bet

    def tie(self):

        self.total += self.bet


values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,'eight':8,
         'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}

suits = ('Hearths', 'Spades','Clubs','Diamonds')

ranks = ('two', 'three', 'four', 'five', 'six', 'seven','eight',
         'nine', 'ten', 'jack', 'queen', 'king', 'ace')

game_on = True
new_deck = Deck()
new_deck.shuffle()
player = Hand('player')
computer = Hand('dealer')
round = 0
player_chips = Chip()
bet = 0

while game_on == True:


    for i in range(2):
        player.hit(new_deck.deal_card())
        computer.hit(new_deck.deal_card())

    try:
        bet = int(input(f"You currently have ({player_chips.total}) chips \nBET: "))
    except:
        print('INVALID KEYS, PLEASE ENTER A NUMBER')
        bet = int(input("BET: "))


    if bet <= player_chips.total:
        player_chips.bet = bet
        player_chips.deposit_chips()
    elif bet > player_chips.total:
        print('You do not have this amount of chips, please try again')
        game_on = False
    else:
        print('problehma')
        game_on = False

    player.display_cards()
    computer.dealer_card()

    decision = input("Press 'Y' to take an additional card or 'N' to to pass: ")

    computer.display_cards()

    while decision.upper() == 'Y':

        player.hit(new_deck.deal_card())
        player.display_given_card()

        val = player.values

        while val < 21:

            dec = input("Do you want to hit again? Press 'Y' to take an additional card or 'N' to to pass: ")
            if dec == 'Y' or dec == 'y':
                player.hit(new_deck.deal_card())
                player.display_given_card()
                player.adjust_for_ace()
                if player.values >= 21:
                    print('You can hit no more')
                    val = 99
            elif dec == 'N' or dec == 'n':
                break

        player.adjust_for_ace()

        while computer.values < 17:
            computer.hit(new_deck.deal_card())
            computer.display_given_card()

        if player.values <=21 and computer.values <=21:

            if player.values > computer.values:

                print(f"Player WINS with: {player.values} over dealer's {computer.values}")
                player_chips.give_chips()
                print(f'total amount of player chips {player_chips.total}')

                player.put_cards_away()
                computer.put_cards_away()

            elif player.values < computer.values and computer.values <=21:

                print(f"Player LOSES with: {player.values} over dealer's {computer.values}")
                print(f'total amount of player chips {player_chips.total}')

                player.put_cards_away()
                computer.put_cards_away()

            elif player.values == computer.values:

                print('DRAW')

                player_chips.tie()
                print(f'total amount of player chips {player_chips.total}')
                player.put_cards_away()
                computer.put_cards_away()

        else:

            if player.values > 21:

                print(f'Player busted')
                print(f'total amount of player chips {player_chips.total}')

                player.put_cards_away()
                computer.put_cards_away()

            elif computer.values > 21:

                print('Dealer busted, player wins')
                player_chips.give_chips()
                print(f'total amount of player chips {player_chips.total}')

                player.put_cards_away()
                computer.put_cards_away()

        if player_chips.total > 0:
            player.aces = 0
            next = input('Press Y if you want to play another round and N if not\n')
            break
        else:
            print('\n\nPlayer out of chips GAME OVER')
            game_on = False
            break


    while decision.upper() == 'N':

        player.adjust_for_ace()

        while computer.values < 17:
            computer.hit(new_deck.deal_card())
            computer.display_given_card()

        computer.adjust_for_ace()

        if player.values > computer.values:

            print(f"Player WINS with: {player.values} over dealer's {computer.values}")
            player_chips.give_chips()
            print(f'total amount of player chips {player_chips.total}')


            player.put_cards_away()
            computer.put_cards_away()


        elif player.values < computer.values and computer.values <=21:

            print(f"Player LOSES with: {player.values} over dealer's {computer.values}")

            print(f'total amount of player chips {player_chips.total}')


            player.put_cards_away()
            computer.put_cards_away()


        elif computer.values > 21:

            print(f'Dealer busted, the player WINS')
            player_chips.give_chips()
            print(f'total amount of player chips {player_chips.total}')


            player.put_cards_away()
            computer.put_cards_away()

        else:

            print('DRAW')

            player_chips.tie()
            player.put_cards_away()
            computer.put_cards_away()

        if player_chips.total > 0:
            player.aces = 0
            next = input('Press Y if you want to play another round and N if not\n')
            break
        else:
            print('\n\nPlayer out of chips GAME OVER')

            game_on = False
            break

    if next == 'n' or 'N':

        game_on == False



