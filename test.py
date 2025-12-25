from enum import Enum



class Winner(Enum):
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    DRAW = 0
    NO_RESULT = -1

def get_value(prop):
    return prop.value



print(get_value(Winner.PLAYER_ONE))