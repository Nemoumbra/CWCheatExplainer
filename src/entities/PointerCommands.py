from CheatEntity import CheatEntity


class PointerCommands(CheatEntity):
    def __init__(self):
        self.address = 0
        self.count = 0
        self.offset = 0
        self.base_offset = 0
