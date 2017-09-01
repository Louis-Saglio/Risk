import missions.base_mission


class DestroyEnnemiMission(missions.base_mission.BaseMission):

    def __init__(self, player, target):
        """
        :type target: player.Player
        """
        super().__init__(player)


    def is_accomplished(self):
        pass
