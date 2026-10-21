from dataclasses import dataclass, field

from .stats import Stats
from .skill import Skill
from .inventory import InventoryItem
from .equipment import Equipment


@dataclass
class Character:

    # Basic Information
    name: str = "New Character"
    race: str = "Human"
    character_class: str = "Adventurer"

    level: int = 1
    experience: int = 0

    # Resources
    gold: int = 0

    hp: int = 100
    max_hp: int = 100

    mana: int = 50
    max_mana: int = 50

    portrait_path: str = ""

    notes: str = ""

    # Complex Structures
    stats: Stats = field(default_factory=Stats)

    skills: list[Skill] = field(default_factory=list)

    inventory: list[InventoryItem] = field(default_factory=list)

    equipment: Equipment = field(default_factory=Equipment)

    def add_skill(self, skill: Skill):
        self.skills.append(skill)

    def add_item(self, item: InventoryItem):
        self.inventory.append(item)

    def calculate_total_weight(self):
        return sum(
            item.weight * item.quantity
            for item in self.inventory
        )

    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "character_class": self.character_class,
            "level": self.level,
            "experience": self.experience,
            "gold": self.gold,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "mana": self.mana,
            "max_mana": self.max_mana,
            "portrait_path": self.portrait_path,
            "notes": self.notes,
            "stats": self.stats.to_dict(),
            "skills": [
                skill.to_dict()
                for skill in self.skills
            ],
            "inventory": [
                item.to_dict()
                for item in self.inventory
            ],
            "equipment": self.equipment.to_dict()
        }

    @classmethod
    def from_dict(cls, data):

        character = cls(
            name=data.get("name", "Unknown"),
            race=data.get("race", "Human"),
            character_class=data.get(
                "character_class",
                "Adventurer"
            ),
            level=data.get("level", 1),
            experience=data.get("experience", 0),
            gold=data.get("gold", 0),
            hp=data.get("hp", 100),
            max_hp=data.get("max_hp", 100),
            mana=data.get("mana", 50),
            max_mana=data.get("max_mana", 50),
            portrait_path=data.get(
                "portrait_path",
                ""
            ),
            notes=data.get("notes", "")
        )

        character.stats = Stats.from_dict(
            data.get("stats", {})
        )

        character.skills = [
            Skill.from_dict(skill)
            for skill in data.get("skills", [])
        ]

        character.inventory = [
            InventoryItem.from_dict(item)
            for item in data.get(
                "inventory",
                []
            )
        ]

        character.equipment = Equipment.from_dict(
            data.get("equipment", {})
        )

        return character