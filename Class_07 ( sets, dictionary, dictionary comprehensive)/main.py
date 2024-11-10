from typing import Dict, Union
import pprint

Key = Union[int, str]
Value = Union[int, str, bool, list, tuple, dict, set]

data: Dict[Key, Value] = {
    1: "a",
    "b": 2,
    3: ["a", "b", "c"],
    "c": {1, 2, 4, 5, 6},
    4: ("a", 1, "b", 2),
    "d": {"abc": 123, 789: "xyz"},
}

pprint.pprint(data)
