import numpy as np
from constants import KEY_NUM, KEY_X, KEY_Y

# define just right hand side
position_cost_right: np.ndarray[np.float64] = np.array(
    [
        [4.0, 2.0, 1.0, 2.0, 6.0],
        [2.0, 0.0, 0.0, 1.0, 3.0],
        [3.0, 1.0, 2.0, 2.0, 5.0],
    ]
)

position_cost = np.hstack([np.fliplr(position_cost_right), position_cost_right]).flatten()

position_pair_cost_right: np.ndarray[np.float64] = np.array(
    [
        [
            [  # (x=5, y=0) -> right hand side
                [1.0, 2.0, 1.0, 1.0, 0.0],
                [3.0, 4.0, 2.0, 1.0, 0.0],
                [4.0, 5.0, 4.0, 2.0, 1.0],
            ],
            [  # (x=6, y=0) -> right hand side
                [2.0, 1.0, 0.0, 0.0, 0.0],
                [4.0, 2.0, 1.0, 0.0, 0.0],
                [4.0, 3.0, 3.0, 1.0, 0.0],
            ],
            [  # (x=7, y=0) -> right hand side
                [1.0, 0.0, 1.0, -1.0, 0.0],
                [1.0, -1.0, 2.0, 0.0, 0.0],
                [2.0, -1.0, 3.0, 2.0, 1.0],
            ],
            [  # (x=8, y=0) -> right hand side
                [1.0, 0.0, -1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 2.0, 1.0],
                [0.0, 0.0, 1.0, 3.0, 2.0],
            ],
            [  # (x=9, y=0) -> right hand side
                [0.0, 0.0, 0.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 3.0, 3.0],
                [0.0, 0.0, 1.0, 6.0, 5.0],
            ],
        ],
        [
            [  # (x=5, y=1) -> right hand side
                [3.0, 4.0, 1.0, 0.0, 0.0],
                [1.0, 3.0, 1.0, 0.0, 0.0],
                [2.0, 3.0, 2.0, 1.0, 0.0],
            ],
            [  # (x=6, y=1) -> right hand side
                [4.0, 2.0, -1.0, 0.0, 0.0],
                [3.0, 1.0, 0.0, 0.0, 0.0],
                [3.0, 2.0, 2.0, 0.0, 0.0],
            ],
            [  # (x=7, y=1) -> right hand side
                [2.0, 1.0, 2.0, 0.0, 0.0],
                [1.0, 0.0, 1.0, -1.0, 0.0],
                [1.0, -1.0, 2.0, 0.0, 0.0],
            ],
            [  # (x=8, y=1) -> right hand side
                [1.0, 0.0, 0.0, 2.0, 3.0],
                [0.0, 0.0, -1.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 2.0, 1.0],
            ],
            [  # (x=9, y=1) -> right hand side
                [0.0, 0.0, 0.0, 1.0, 3.0],
                [0.0, 0.0, 0.0, 1.0, 1.0],
                [0.0, 0.0, 0.0, 3.0, 3.0],
            ],
        ],
        [
            [  # (x=5, y=2) -> right hand side
                [4.0, 4.0, 2.0, 0.0, 0.0],
                [2.0, 3.0, 1.0, 0.0, 0.0],
                [1.0, 2.0, 1.0, 1.0, 0.0],
            ],
            [  # (x=6, y=2) -> right hand side
                [5.0, 3.0, -1.0, 0.0, 0.0],
                [3.0, 2.0, -1.0, 0.0, 0.0],
                [2.0, 1.0, 0.0, 0.0, 0.0],
            ],
            [  # (x=7, y=2) -> right hand side
                [4.0, 3.0, 3.0, 1.0, 1.0],
                [2.0, 2.0, 2.0, 0.0, 0.0],
                [1.0, 0.0, 1.0, -1.0, 0.0],
            ],
            [  # (x=8, y=2) -> right hand side
                [2.0, 1.0, 2.0, 3.0, 6.0],
                [1.0, 0.0, 0.0, 2.0, 3.0],
                [1.0, 0.0, -1.0, 1.0, 1.0],
            ],
            [  # (x=9, y=2) -> right hand side
                [1.0, 0.0, 1.0, 2.0, 5.0],
                [0.0, 0.0, 0.0, 1.0, 3.0],
                [0.0, 0.0, 0.0, 1.0, 1.0],
            ],
        ],
    ],
)

# connext with generated left hand side
position_pair_cost_right = np.concatenate(
    (np.full((KEY_Y, KEY_X // 2, KEY_Y, KEY_X // 2), 0.0, dtype=np.float64), position_pair_cost_right), axis=3
)
position_pair_cost: np.ndarray[np.float64] = np.concatenate(
    (position_pair_cost_right[..., ::-1, :, ::-1], position_pair_cost_right), axis=1
).reshape(KEY_NUM, KEY_NUM)

if __name__ == "__main__":

    def position_pair_cost_to_str():
        ret: str = ""
        for i in range(30):
            ret += f"i: {i}\n"
            ret += f"{position_pair_cost[i].reshape(KEY_Y, KEY_X)}\n"
        return ret

    print(position_pair_cost_to_str())
