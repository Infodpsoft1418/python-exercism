from collections import defaultdict


line_fmt = "{0:30} | {1:2} | {2:2} | {3:2} | {4:2} | {5:2}"


class Team:
    def __init__(self):
        self.name = ""
        self.wins = 0
        self.loses = 0
        self.draws = 0

    @property
    def score(self):
        return self.wins * 3 + self.draws

    @property
    def played(self):
        return self.wins + self.loses + self.draws

    def __str__(self):
        return self.name

    def won(self):
        self.wins += 1

    def loss(self):
        self.loses += 1

    def draw(self):
        self.draws += 1

    def print_row(self):
        return line_fmt.format(
            self.name, self.played, self.wins, self.draws, self.loses, self.score,
        )


def format_table(results):
    x = results.copy()
    header = line_fmt.format("Team", "MP", " W", " D", " L", " P")
    result = sorted(results.values(), key=lambda t: (-t.score, t.name))
    table = [header]
    for team in result:
        table.append(team.print_row())
    return table


def parse_game(game, results):
    home, road, result = game.split(";")
    results[home].name = home
    results[road].name = road
    if result == "win":
        results[home].won()
        results[road].loss()
    elif result == "loss":
        results[home].loss()
        results[road].won()
    elif result == "draw":
        results[home].draw()
        results[road].draw()
    return results


def tally(rows):
    results = defaultdict(Team)
    for row in rows:
        results = parse_game(row, results)
    return format_table(results)
