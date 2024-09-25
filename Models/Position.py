class Position:
    def __init__(self,id, name):
        self.id = id
        self.name = name
        self.isDefender = id > 0 and id <= 3
        self.isGoalKeeper = id == 1
        self.isManager = id == 6