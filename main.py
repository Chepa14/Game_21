from terminal_playing_cards import Deck
from terminal_playing_cards import View
import time


class Game:
    def __init__(self):
        self.is_active = True
        self.deck = Cards()
        self.players = [Player(
            input("Enter your name: "),
            self.deck.get_cards()
        ),
            Dealer(
                self.deck.get_cards()
            )
        ]

    def create_game(self):
        print(" ____________________________\n"
              "|AVAILABLE MOVES:            |\n"
              "|(1) - Hit card (Get a card).|\n"
              "|(2) - Stands (Pass cards).  |\n"
              "|(0) - Quit the game.        |\n"
              " ____________________________\n")
        time.sleep(1)
        while self.is_active:
            self.play_game()
        print("\nGAME ENDED!\n")
        self.restart_game()

    def restart_game(self):
        answer = input("Do you want to play again [Y/N]?  ")
        if answer in ("Y", "y", "yes", "Yes", "YES"):
            new_game = Game()
            new_game.create_game()

    def player_move(self, player):
        self.deck.print_cards(player)
        while not player.is_stand:
            action = player.process_input()
            action(self, player)

    def play_game(self):
        for player in self.players:
            if self.is_active:
                self.player_move(player)
        self.find_winner()

    def hit_card(self, player):
        player.add_card(self.deck.get_cards(1))
        self.deck.print_cards(player)
        if player.check_sum():
            self.output(player, "Sum of cards goes over 21! Player lost!")
            player.is_stand = True
            player.is_lose = True
            # self.is_active = False   # Remove comment if you want to play without DRAW

    def stand(self, player):
        self.output(player, "Stands!")
        player.is_stand = True

    def quit(self, player):
        self.output(player, "Quit the game!")
        player.is_stand = True
        player.is_lose = True
        self.is_active = False

    def find_winner(self):
        candidates = [player for player in self.players if not player.is_lose]
        if len(candidates) == 0:
            print("*  DRAW!  *")
        elif len(candidates) == 1:
            print(f"*  {candidates[0].name} - WINNER!  *")
        else:
            winner = max(candidates, key=lambda player: player.sum_of_cards)
            print(f"*  {winner.name} - WINNER!  *")
        self.is_active = False

    def output(self, curr_player, text):
        print(f"[{curr_player.name}] {text} \n")


class Player:

    def __init__(self, name, cards):
        self.rules = {
            "1": Game.hit_card,
            "2": Game.stand,
            "0": Game.quit
        }
        self.name = name
        self.is_stand = False
        self.is_lose = False
        self.cards = cards
        self.sum_of_cards = self.get_sum_of_cards()

    def process_input(self, value=None):
        decision = self.rules.get(value, -1)
        if decision == -1:
            decision = self.process_input(input('Make your decision: '))
        return decision

    def check_sum(self):
        if self.sum_of_cards > 21:
            return True
        return False

    def get_sum_of_cards(self):
        sum = 0
        for card in self.cards:
            sum += card.value
        return sum

    def update_sum(self):
        self.sum_of_cards = self.get_sum_of_cards()

    def add_card(self, card):
        self.cards.extend(card)
        self.update_sum()


class Dealer(Player):
    def __init__(self, cards):
        super().__init__("Dealer", cards)

    def process_input(self, value=None):
        time.sleep(1.5)
        if self.sum_of_cards < 17:
            return super(Dealer, self).process_input("1")
        else:
            return super(Dealer, self).process_input("2")


class Cards:
    CUSTOM_DECK_SPEC = {
        "A": {"clubs": 11, "diamonds": 11, "spades": 11, "hearts": 11},
        "2": {"clubs": 2, "diamonds": 2, "spades": 2, "hearts": 2},
        "3": {"clubs": 3, "diamonds": 3, "spades": 3, "hearts": 3},
        "4": {"clubs": 4, "diamonds": 4, "spades": 4, "hearts": 4},
        "5": {"clubs": 5, "diamonds": 5, "spades": 5, "hearts": 5},
        "6": {"clubs": 6, "diamonds": 6, "spades": 6, "hearts": 6},
        "7": {"clubs": 7, "diamonds": 7, "spades": 7, "hearts": 7},
        "8": {"clubs": 8, "diamonds": 8, "spades": 8, "hearts": 8},
        "9": {"clubs": 9, "diamonds": 9, "spades": 9, "hearts": 9},
        "10": {"clubs": 10, "diamonds": 10, "spades": 10, "hearts": 10},
        "J": {"clubs": 2, "diamonds": 2, "spades": 2, "hearts": 2},
        "Q": {"clubs": 3, "diamonds": 3, "spades": 3, "hearts": 3},
        "K": {"clubs": 4, "diamonds": 4, "spades": 4, "hearts": 4},
    }

    def __init__(self):
        self.deck = self.create_shuffle_deck()

    def create_shuffle_deck(self):
        deck = Deck(self.CUSTOM_DECK_SPEC)
        deck.shuffle()
        return deck

    def get_cards(self, count=2):
        return [self.deck.pop() for _ in range(count)]

    def print_cards(self, player):
        print(f"[{player.name}] CARDS:")
        print(View(player.cards))
        print(f"SUM OF CARDS: {player.sum_of_cards}")


if __name__ == '__main__':
    game = Game()
    game.create_game()
