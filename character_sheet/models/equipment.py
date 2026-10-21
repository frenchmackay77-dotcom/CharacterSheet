from dataclasses import dataclass


@dataclass
class Equipment:
    head: str = ""
    chest: str = ""
    legs: str = ""
    feet: str = ""

    main_hand: str = ""
    off_hand: str = ""

    ring_1: str = ""
    ring_2: str = ""

    necklace: str = ""

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)