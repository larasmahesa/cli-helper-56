import random

class GameProcessor:
    def __init__(self, players):
        self.players = players
        self.scores = {player: 0 for player in players}

    def roll_dice(self):
        return random.randint(1, 6)

    def play_round(self):
        for player in self.players:
            roll = self.roll_dice()
            self.scores[player] += roll
            print(f'{player} rolled a {roll}. Total score: {self.scores[player]}')

    def declare_winner(self):
        winner = max(self.scores, key=self.scores.get)
        print(f'The winner is {winner} with a score of {self.scores[winner]}!')

    def play_game(self, rounds):
        for _ in range(rounds):
            self.play_round()
        self.declare_winner()

if __name__ == '__main__':
    players = ['Alice', 'Bob', 'Charlie']
    game = GameProcessor(players)
    game.play_game(5)