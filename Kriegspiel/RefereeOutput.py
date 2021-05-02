"""
Define base classes of referee output
"""

class RefereeOutput():
    def __init__(self, for_player, from_cell=None, to_cell=None, moves_made=None, additional_text="", *args, **kwargs):
        self.label = None
        self.for_player = for_player
        self.from_cell = from_cell
        self.to_cell = to_cell
        self.success = None
        self.additional_text = additional_text
        self.moves_made = moves_made

    def __str__(self):
        return "@{p} - {l} {e}".format(p=self.for_player, l=self.label, e=self.additional_text)

class LegalMove(RefereeOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success = True

class IllegalMove(RefereeOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success = False


"""
When a legal move is made
"""

class Okay(LegalMove):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "Move was legal."


class OkayTaken(LegalMove):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "Move was legal and a piece was taken."


"""
When an illegal move is attempted
"""

class Blocked(IllegalMove):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "Move is blocked"


class Impossible(IllegalMove):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.label = "Move is impossible"
        
"""
Check announcements
"""

class Check(RefereeOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DiagonalCheck(Check):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "You are in diagonal check."

class LongDiagonalCheck(Check):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "You are in long diagonal check."

class KnightCheck(Check):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "You are in check by a Knight."

class RowCheck(Check):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "You are in row-check."

class ColumnCheck(Check):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "You are in column-check."

class CheckMate(Check):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "You are in check mate."

class GameOver(RefereeOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = "Game over!"
