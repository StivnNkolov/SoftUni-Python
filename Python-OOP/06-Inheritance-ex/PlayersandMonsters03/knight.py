from PlayersandMonsters03.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)


#
# test_knight = Knight("THIS IS KNIGHT", 1)
# print(test_knight)