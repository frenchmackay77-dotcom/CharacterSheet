from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    quantity: int = 1
    value: int = 0
    weight: float = 0.0

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "value": self.value,
            "weight": self.weight
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)