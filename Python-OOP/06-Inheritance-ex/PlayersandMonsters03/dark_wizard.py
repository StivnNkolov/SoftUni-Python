from PlayersandMonsters03.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)


# test = DarkWizard("THIS IS DARKWIZARD", 19)
# print(test)