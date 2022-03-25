from typing import List
import numpy as np

spirits = ["Vodka", "Rum", "White Rum", "Spiced Rum", "Gin", "Absinthe", "Whiskey", "Brandy", "Tequila", "Sambuka"]
mixers = ["Coke", "Fanta", "Orange Juice", "Chocolate Milk", "Oatly", "Water", "Villa", "Lemonade", "Apple Juice"]

players = ["Ben", "Sam", "Luis", "Quandale"]

def reduced_ratio(int1: int, int2: int) -> int:
    gcd = np.gcd.reduce([int1, int2])

    return int(int1/gcd), int(int2/gcd)

np.random.shuffle(spirits)
np.random.shuffle(mixers)

for i in range(len(players)):
    player = players[i]
    spirit = spirits[i]
    mixer = mixers[i]
    ratio1, ratio2 = reduced_ratio(np.random.randint(3, size=1)[0] + 1, np.random.randint(5, size=1)[0] + 1)

    print(f"{player} will be drinking {spirit} with {mixer} at a ratio of {ratio1}:{ratio2}")