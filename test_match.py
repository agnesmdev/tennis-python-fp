from match import Match


def test_initial_score_should_be_love_to_love():
    assert Match().result() == "love all"


def test_game_result_should_be_fifteen_to_love_when_player1_scores():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    # Assert
    assert m.result() == "fifteen to love"


def test_game_result_should_be_thirty_to_love_when_player1_scores_twice():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player1.score()
    # Assert
    assert m.result() == "thirty to love"


def test_game_result_should_be_forty_to_love_when_player1_scores_three_times():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player1.score()
    m.player1.score()
    # Assert
    assert m.result() == "forty to love"


def test_game_result_should_be_game_when_player1_scores_four_times():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player1.score()
    m.player1.score()
    m.player1.score()
    # Assert
    assert m.result() == "player1 wins game"


def test_game_result_should_be_love_to_fifteen_when_player2_scores():
    # Arrange
    m = Match()
    # Act
    m.player2.score()
    # Assert
    assert m.result() == "love to fifteen"


def test_game_result_should_be_fifteen_all_when_both_players_score():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player2.score()
    # Assert
    assert m.result() == "fifteen all"


def test_game_result_should_be_thirty_all_when_both_players_score_twice():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player2.score()
    m.player1.score()
    m.player2.score()
    # Assert
    assert m.result() == "thirty all"


def test_game_result_should_be_deuce_when_both_players_score_three_times():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player2.score()
    m.player1.score()
    m.player2.score()
    m.player1.score()
    m.player2.score()
    # Assert
    assert m.result() == "deuce"


def test_game_result_should_be_advantage_player2_when_player1_score_three_times_and_player2_four_times():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player2.score()
    m.player1.score()
    m.player2.score()
    m.player1.score()
    m.player2.score()
    m.player2.score()
    # Assert
    assert m.result() == "advantage player2"


def test_game_result_should_be_game_when_player2_scores_four_times():
    # Arrange
    m = Match()
    # Act
    m.player2.score()
    m.player2.score()
    m.player2.score()
    m.player2.score()
    # Assert
    assert m.result() == "player2 wins game"


def test_game_result_should_be_advantage_player1_when_player2_score_three_times_and_player1_four_times():
    # Arrange
    m = Match()
    # Act
    m.player1.score()
    m.player2.score()
    m.player1.score()
    m.player2.score()
    m.player1.score()
    m.player2.score()
    m.player1.score()
    # Assert
    assert m.result() == "advantage player1"


def test_game_result_should_be_game_when_player2_scores_six_times_and_player1_four_times():
    # Arrange
    m = Match()
    # Act
    m.player2.score()
    m.player2.score()
    m.player2.score()
    m.player2.score()
    m.player2.score()
    m.player2.score()
    m.player1.score()
    m.player1.score()
    m.player1.score()
    m.player1.score()
    # Assert
    assert m.result() == "player2 wins game"
