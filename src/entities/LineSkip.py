from CheatEntity import CheatEntity
from enum import Enum, auto


class CheckType(Enum):
    IfEqual = 0
    IfNotEqual = auto()
    IfLess = auto()
    IfGreater = auto()

    IfAddressEqual = auto()
    IfAddressNotEqual = auto()
    IfAddressLess = auto()
    IfAddressGreater = auto()


class LineSkip(CheatEntity):
    def __init__(self):
        self.size = 0
        self.address = 0
        self.check = CheckType.IfEqual
        self.skip_count = 0

