from CheatEntity import CheatEntity


class JokerCode(CheatEntity):
    def __init__(self):
        self.keys_mask = 0
        self.inverse = False
        self.skip_count = 0
