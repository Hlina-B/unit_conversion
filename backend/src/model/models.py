from enum import Enum
from dataclasses import dataclass

class Parameters(Enum):
    VALUE = "value"
    FROM_UNIT = "from_unit"
    TO_UNIT = "to_unit"
    BASE_UNIT = "base_unit"

@dataclass
class ConversionResponse:
    original_value: float
    from_unit: str
    converted_value: float
    to_unit: str
