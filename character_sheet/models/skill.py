from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    level: int = 1
    description: str = ""

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    