from pydantic import BaseModel, Field
from numpy import median
from enum import Enum

class Result(Enum):
    P1 = 1
    P2 = -1
    DRAW = 0
    NO_RESULT = 88

class Rating(BaseModel):
    rating: tuple[float, float] = Field(serialization_alias="r0", default=(0, 0))
    score: tuple[float, float] = Field(serialization_alias="s0", default=(0, 0))
    
    def __init__ (self, r0 : tuple | list = (0, 0), s : tuple | list = (0, 0)):
        super().__init__(rating=r0, score=s)
        
        self._winner = self._determine_winner()
        self._median = self._calc_median()
        self._difference = self._calc_difference()
        self._scaling = self._calc_scaling()
        
    def __str__(self) -> str:
        return f"{self._winner} {self._median} {self._scaling}"
    
    # region Determination methods
    def _determine_winner(self):
        if (self.score[0] > self.score[1]):
            return Result.P1
        if (self.score[0] < self.score[1]):
            return Result.P2
        if (self.score[0] == self.score[1]):
            return Result.DRAW
        
        return Result.NO_RESULT
    # endregion
    # region Calculation helper methods
    def _calc_median(self):
        return float(median(self.rating))
    
    def _calc_difference(self):
        difference = round((self.rating[0] - self.rating[1]), 2)
        return -difference if difference < 0 else difference
    
    def _calc_scaling(self):
        scaling = round((self._difference / self._median * 100), 2)
        return -scaling if scaling < 0 else scaling
    # endregion
    
    # region Misc helper functions
    
rating = Rating([1000, 200], [1, 2])
print(rating)