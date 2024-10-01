from Models.Position import Position
from enum import Enum

class Athlete:
    def __init__(self, id, nickname, position, team_id, price, scouts,
                 avg_score, status_id):
        self.id = id
        self.nickname = nickname
        self.position = position
        self.team_id = team_id
        self.price = price
        self.scouts = scouts
        self.avg_score = avg_score
        self.status_id = status_id
        self.AthleteInfo = []


class AthleteInfo(Enum):
    MOST_GOALS = 1
    MOST_ASSISTS = 2
    MOST_STEALS = 3
    MOST_SAVES = 4
    MOST_CLEAN_SHEETS = 5  # defenders only
    MOST_SHOTS_SAVED = 6  # goalkeeper only
    MOST_SHOTS_MISSED = 7
    MOST_SHOTS_AT_POST = 8
    MOST_FOULED = 9
    MOST_FOULS_MADE = 10
    MOST_CARDS_TAKEN = 11
    HIGHEST_AVG_SCORE = 12
    MOST_WINS = 13  # manager only 
