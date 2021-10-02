class Game:

    rules = {
        "1": "Hit (Get card)",
        "2": "Stands (Pass cards)",
        "0": "Quit"
    }

    def __init__(self):
        self.is_active = True
        self.players = [Player(
            input("Enter your name: "),
            ['2', '3']
        ),
            Dealer(['1', '6'])
        ]

    def create_game(self):
        while self.is_active:
            self.play_game()
            print("Game ended!")

    def process_input(self, value=None):
        decision = self.rules.get(value, -1)
        if decision == -1:
            decision = self.process_input(input('Make your decision: '))
        return decision

    def player_move(self, player):

        print(f"[{player.name}] Your's cards:")
        print(f"{player.cards}")
        while True:
            action = self.process_input()
            if action == "Quit":
                self.output(player, "Quit the game")
                self.is_active = False
                break
            else:
                self.output(player, action)
                if player.check_sum():
                    self.output(player, "Sum of cards goes over 21! You are lost!")

    def output(self, curr_player, text):
        print(f"[{curr_player.name}] {text}")

    def play_game(self):
        for player in self.players:
            if self.is_active:
                self.player_move(player)


class Player:

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards  # TODO give this from class Cards
        self.sum_of_cards = 0

    def get_card(self):
        card = self.cards.get_new_card()
        card_value = self.cards.get_card_value(card)
        self.sum_of_cards += card_value

    def check_sum(self):
        if self.sum_of_cards > 21:
            return True
        return False

    def get_sum_of_cards(self):
        return self.sum_of_cards


class Dealer(Player, Game):
    def __init__(self, cards):
        super().__init__("Dealer", cards)

    def get_card(self):  # TODO add rules
        super(Dealer, self).get_card()

    def process_input(self, value=None):
        if self.sum_of_cards < 17:
            return super(Dealer, self).process_input("1")
        else:
            return super(Dealer, self).process_input("2")


class Cards:

    def __init__(self):
        # TODO create list of cards
        ...  # TODO random sort cards


if __name__ == '__main__':
    game = Game()
    game.create_game()
