class BaseMission:

    def __init__(self, player):
        """
        :type player: player.Player
        """
        self.player = player

    def is_accomplished(self):
        raise NotImplementedError
