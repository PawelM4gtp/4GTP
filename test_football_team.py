

from football_team import FootballTeam


def test_team_initialization():
    team = FootballTeam("FC Python")
    assert team.team_name == "FC Python"
    assert team.players == {}


def test_add_player():
    team = FootballTeam("FC Python")
    team.add_player("John", 5)
    assert "John" in team.players
    assert team.players["John"] == 5


def test_get_player_goals():
    team = FootballTeam("FC Python")
    team.add_player("John", 5)
    goals = team.get_player_goals("John")
    assert goals == 5


def test_get_nonexistent_player_goals():
    team = FootballTeam("FC Python")
    goals = team.get_player_goals("Jane")
    assert goals == 0


def test_remove_player():
    team = FootballTeam("FC Python")
    team.add_player("John", 5)
    team.remove_player("John")
    assert "John" not in team.players


def test_team_average_goals():
    team = FootballTeam("FC Python")
    team.add_player("John", 5)
    team.add_player("Jane", 3)
    assert team.get_team_average_goals() == 4.0


def test_team_average_goals_empty():
    team = FootballTeam("FC Python")
    assert team.get_team_average_goals() == 0


def test_player_exists():
    team = FootballTeam("FC Python")
    team.add_player("John", 5)
    assert team.player_exists("John") is True
    assert team.player_exists("Jane") is False


def test_get_players():
    team = FootballTeam("FC Python")
    team.add_player("John", 5)
    team.add_player("Jane", 3)
    players = team.get_players()
    assert "John" in players
    assert "Jane" in players

#
def test_remove_player_from_empty_team():
    team = FootballTeam("FC Python")
    team.remove_player("John")
    assert team.players == {}


def test_add_player_with_negative_goals():
    team = FootballTeam("FC Python")
    team.add_player("John", -5)
    assert team.players["John"] == -5


def test_team_average_goals_with_negative_values():
    team = FootballTeam("FC Python")
    team.add_player("John", -3)
    team.add_player("Jane", 5)
    assert team.get_team_average_goals() == 1.0


def test_add_player_with_zero_goals():
    team = FootballTeam("FC Python")
    team.add_player("John", 0)
    assert team.players["John"] == 0


def test_remove_last_player():
    team = FootballTeam("FC Python")
    team.add_player("John", 5)
    team.remove_player("John")
    assert team.get_players() == []


def test_add_large_number_of_players():
    team = FootballTeam("FC Python")
    for i in range(1000):
        team.add_player(f"Player{i}", i)
    average_goals = team.get_team_average_goals()
    expected_average = sum(range(1000)) / 1000
    assert average_goals == expected_average
