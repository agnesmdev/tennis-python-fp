class Player:

    def __init__(self):
        self.points = 0

    points: int

    def score(self) -> int:
        self.points = self.points + 1
        return self.points


class Referee:
    points_to_result = {
        0: "love",
        1: "fifteen",
        2: "thirty",
        3: "forty"
    }

    def who_wins(self, player1_points, player2_points) -> str:
        points_difference = abs(player1_points - player2_points)
        if (player1_points >= 4 & points_difference >= 2):
            return "player1"
        if (player2_points >= 4 & points_difference >= 2):
            return "player2"
        return None

    def who_has_advantage(self, player1_points, player2_points) -> str:
        if (player2_points > player1_points & player1_points >= 3):
            return "player2"
        if (player1_points > player2_points & player2_points >= 3):
            return "player1"
        return None

    def is_even(self, player1_points, player2_points) -> bool:
        return player1_points == player2_points

    def is_deuce(self, player1_points, player2_points) -> bool:
        return (player1_points == player2_points) & (player1_points == 3)

    def announces(self, player1_points, player2_points) -> str:
        winner = self.who_wins(player1_points, player2_points)
        if winner is not None:
            return winner + " wins game"
        if self.is_deuce(player1_points, player2_points):
            return "deuce"
        player1_result = self.points_to_result.get(player1_points, "N/A")
        if self.is_even(player1_points, player2_points):
            return player1_result + " all"
        player_in_the_lead = self.who_has_advantage(player1_points, player2_points)
        if player_in_the_lead is not None:
            return "advantage " + player_in_the_lead
        player2_result = self.points_to_result.get(player2_points, "N/A")
        return player1_result + " to " + player2_result


class Match:

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.referee = Referee()

    def result(self) -> str:
        return self.referee.announces(self.player1.points, self.player2.points)

        # should be immutable

    player1: Player
    player2: Player
    referee: Referee
