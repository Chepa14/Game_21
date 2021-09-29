import icecream as ic


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
            return False
        return True

    def get_sum_of_cards(self):
        return self.sum_of_cards


class Dealer(Player):
    def __init__(self, name, cards):
        super().__init__("Dealer", cards)

    def get_card(self):  # TODO add rules
        super(Dealer, self).get_card()


class Cards:

    def __init__(self):
        # TODO create list of cards
        ...  # TODO random sort cards


class Game:

    def __init__(self):
        self.is_active = True

    def play_game(self):
        ...


if __name__ == '__main__':
    game = Game()
    while game.is_active:
        game.play_game()
