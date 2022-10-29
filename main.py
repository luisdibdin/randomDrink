import numpy as np
from typing import List, Tuple, Dict, Any
from pathlib import Path
import yaml
import random
from dataclasses import dataclass


def load_yaml_values(path: Path, file_name: str) -> List[Any]:
    with open(path / file_name) as f:
        config = yaml.safe_load_all(f)
        config = next(config)

    return list(config.values())[0]


def reduce_ratio(int1: int, int2: int) -> Tuple[int, int]:
    gcd = np.gcd.reduce([int1, int2])

    return int(int1 / gcd), int(int2 / gcd)


config_path = Path("config")
config: Dict[str, List[Any]] = {
    f.stem: load_yaml_values(config_path, f.name) for f in config_path.iterdir()
}

players = config.get("players", [])
spirits = config.get("spirits", [])
mixers = config.get("mixers", [])

np.random.shuffle(spirits)
np.random.shuffle(mixers)

for player in players:
    spirit = spirits.pop()
    mixer = mixers.pop()
    ratio1, ratio2 = reduce_ratio(
        np.random.randint(3, size=1)[0] + 1, np.random.randint(5, size=1)[0] + 1
    )

    print(
        f"{player} will be drinking {spirit} with {mixer} at a ratio of {ratio1}:{ratio2}"
    )
