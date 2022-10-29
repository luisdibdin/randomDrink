import random
import numpy as np
from typing import List, Tuple, Dict, Any
from pathlib import Path
import yaml


def load_yaml_values(path: Path, file_name: str) -> List[Any]:
    with open(path / file_name) as f:
        config = yaml.safe_load_all(f)
        config = next(config)

    return list(config.values())[0]


def reduce_ratio(int1: int, int2: int) -> Tuple[int, int]:
    gcd = np.gcd.reduce([int1, int2])

    return int(int1 / gcd), int(int2 / gcd)


class RandomDrink:
    def __init__(self, config: Dict[str, List[Any]]) -> None:
        self.players = config.get("players", [])
        self.spirits = config.get("spirits", [])
        self.mixers = config.get("mixers", [])

    def run(self) -> None:
        out = map(self.construct_sentence, self.players)
        print(*out, sep="\n")

    def construct_sentence(self, player) -> str:
        return f"{player} will be drinking {self.random_spirit()} with {self.random_mixer()} at a ratio of {self.construct_ratio()}"

    def random_spirit(self) -> str:
        return random.choice(self.spirits)

    def random_mixer(self) -> str:
        return random.choice(self.mixers)

    def construct_ratio(self) -> str:
        ratio1, ratio2 = reduce_ratio(
            np.random.randint(3, size=1)[0] + 1, np.random.randint(5, size=1)[0] + 1
        )

        return f"{ratio1}:{ratio2}"


def main() -> None:
    config_path = Path("config")
    config: Dict[str, List[Any]] = {
        f.stem: load_yaml_values(config_path, f.name) for f in config_path.iterdir()
    }
    random_drink = RandomDrink(config)
    random_drink.run()


if __name__ == "__main__":
    main()
