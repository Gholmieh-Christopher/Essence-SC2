# Written by: Christopher Gholmieh
# Imports:

# Dataclasses:
import dataclasses

# Classes:
@dataclasses.dataclass
class Enumeration:
    """
    Base class for enumerations.
    
    :param value:
    :param name:
    """
    
    value: int
    name: str
    
    # Special Methods:
    def __eq__(self, other_enumeration) -> bool:
        """
        Returns a boolean comparing if this enumeration and the other enumeration are the same.
        """
        
        return (
            other_enumeration.value == self.value and
            other_enumeration.name == self.name
        )
