from GuildSystem.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != "Unaffiliated" and player not in self.players:
            return f"Player {player.name} is in another guild."
        if player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, name):
        for player1 in self.players:
            if player1.name == name:
                self.players.remove(player1)
                player1.guild = "Unaffiliated"
                return f"Player {name} has been removed from the guild."
        return f"Player {name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" \
               f"{''.join([p.player_info() for p in self.players])}"


player_one = Player("Stivan", 200, 100)
player_two = Player("Martin", 450, 50)

# print(player_one.player_info())

player_one.add_skill("Fire bolt", 20)

# print(player_one.player_info())

# print(player_one.add_skill("Snare", 15))

print(player_one.player_info())


first_guild = Guild("League of legends")
second_guild = Guild("Counter strike")

print(first_guild.assign_player(player_one))

print(second_guild.assign_player(player_one))

print(first_guild.assign_player(player_one))

first_guild.assign_player(player_two)

print(first_guild.kick_player("Stivan"))

print(first_guild.kick_player("Stivan"))

first_guild.assign_player(player_one)
print()
print()

print(first_guild.guild_info())

print(second_guild.guild_info())
print()
print()
print()
print(first_guild.guild_info())

print(first_guild.kick_player("Stivan"))







