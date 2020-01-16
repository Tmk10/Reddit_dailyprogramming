
class CardFlippingGame:

    def __init__(self, cards):
        self.cards = {index:status for index, status in zip(range(len(cards)), [1 if card == "1" else 0 for card in cards])}
        self.moves = []

    def solve_game(self):

        while not self.check_status():
            for index in self.calculate_possible_flips():
                self.moves.append(index)
                self.flip_card(index)
                if self.check_status():
                    print(self.moves)
                    return
                else:
                    return self.solve_game()
            print("No solution")
            return

    def check_status(self):
        if len(set(self.cards.values())) != 1:
            return False
        else:
            return True

    def calculate_possible_flips(self):
        return [key for key in self.cards.keys() if self.cards[key] == 1]

    def flip_card(self, card_index):
        self.cards[card_index] = -1
        adjacent_indexes = (card_index -1, card_index +1)
        for index in adjacent_indexes:
            if 0 <= index <= len(self.cards) -1:
                if self.cards[index] == 1:
                    self.cards[index] = 0
                elif self.cards[index] == 0:
                    self.cards[index] = 1

inputs= ["0100110",
"001011011101001001000",
"1010010101001011011001011101111",
"1101110110000001010111011100110",
"010111111111100100101000100110111000101111001001011011000011000"]


for input in inputs:
    game = CardFlippingGame(input)
    print(input)
    game.solve_game()
