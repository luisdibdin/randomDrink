from typing import List
import numpy as np

spirits = ["Vodka", "Rum", "White Rum", "Spiced Rum", "Gin", "Absinthe", "Whiskey", "Brandy", "Tequila", "Sambuka"]
mixers = ["Coke", "Fanta", "Orange Juice", "Chocolate Milk", "Oatly", "Water", "Villa", "Lemonade", "Apple Juice"]

players = ["Ben", "Sam", "Luis", "Quandale"]

def reduce_ratio(ratio_list: List[int]) -> List[int]:
    gcd = np.gcd.reduce(ratio_list)
    ratio_list_reduced = [int(i/gcd) for i in ratio_list]

    return ratio_list_reduced

np.random.shuffle(spirits)
np.random.shuffle(mixers)

for i in range(len(players)):
    player = players[i]
    spirit = spirits[i]
    mixer = mixers[i]
    ratio_list_reduced = reduce_ratio([np.random.randint(3, size=1)[0] + 1, np.random.randint(5, size=1)[0] + 1])

    print(f"{player} will be drinking {spirit} with {mixer} at a ratio of {ratio_list_reduced[0]}:{ratio_list_reduced[1]}")