# Written by: Christopher Gholmieh
# Imports:

# Classes:
class Enumeration:
    # Initialization:
    def __init__(self, value: int, name: str) -> None:
        # Integers:
        self.value: int = value

        # Strings:
        self.name: str = name

    # Magic Methods:
    def __eq__(self, other_enumeration) -> bool:
        return (
            self.value == other_enumeration.value
            and self.name == other_enumeration.name
        )
