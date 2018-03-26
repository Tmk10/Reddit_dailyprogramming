from random import choice, choices, shuffle

deck = [(str(x), y) for x in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] for y in "♠♥♦♣"]


class Blackjack():
    def __init__(self, decks):
        self.bj_deck = decks * deck

    def hit(self, cards=None):
        shuffle(self.bj_deck)
        if len(self.bj_deck) < 3:
            return "End of cards in deck"
        elif cards is None:
            cards = choices(self.bj_deck, k=2)
            for card in cards:
                self.bj_deck.remove(card)
        else:
            cards.append(choice(self.bj_deck))
            self.bj_deck.remove(cards[-1])
        self.points = []
        for card in cards:
            if card[0].isdigit():
                self.points.append(int(card[0]))
            else:
                if card[0] == "A" and 11 not in self.points:
                    self.points.append(11)
                elif card[0] == "A" and 11 in self.points:
                    self.points[self.points.index(11)] = 1
                    self.points.append(1)
                elif card[0] == "A" and 1 in self.points:
                    self.points.append(1)
                elif card[0] == "J" or "Q" or "K":
                    self.points.append(10)
        if sum(self.points) > 10:
            return "".join([item for card in cards for item in card]), sum(self.points)
        else:
            while sum(self.points) <= 10 and len(cards) <=2:
                self.hit(cards)
        return "".join([item for card in cards for item in card]), sum(self.points)


def play_bj(games):
    game = Blackjack(10)
    counter = 0
    for i in range(games):
        result = game.hit()
        if result[1] == 21:
            counter += 1
    print("After {} games was {} blackjacks at %{:.1f}".format(games,counter,(counter/games) *100))



