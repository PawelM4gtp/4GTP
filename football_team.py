# football_team.py

class FootballTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = {}

    def add_player(self, player_name, goals):
        """Dodaj zawodnika do drużyny z liczbą goli."""
        self.players[player_name] = goals

    def get_player_goals(self, player_name):
        """Zwróć liczbę goli danego zawodnika."""
        return self.players.get(player_name, 0)

    def get_team_average_goals(self):
        """Zwróć średnią liczbę goli na zawodnika w drużynie."""
        if len(self.players) == 0:
            return 0
        total_goals = sum(self.players.values())
        return total_goals / len(self.players)

    def remove_player(self, player_name):
        """Usuń zawodnika z drużyny."""
        if player_name in self.players:
            del self.players[player_name]

    def get_players(self):
        """Zwróć listę wszystkich zawodników w drużynie."""
        return list(self.players.keys())

    def player_exists(self, player_name):
        """Sprawdź, czy zawodnik istnieje w drużynie."""
        return player_name in self.players
