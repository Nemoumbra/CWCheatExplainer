from CheatEntity import CheatEntity


class PatchMultiWrite(CheatEntity):
    def __init__(self):
        self.start = 0
        self.count = 0
        self.size = 0
        self.step = 0
        self.value = 0
        self.value_step = 0
