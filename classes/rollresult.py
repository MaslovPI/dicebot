from dataclasses import dataclass


@dataclass
class RollResult:
    def __init__(self, rolls):
        self.rolls = list(rolls)

    @property
    def total(self):
        return sum(self.rolls)

    def describe(self):
        rolls_str = ", ".join(str(n) for n in self.rolls)
        return f"{self.total} ({rolls_str})"
