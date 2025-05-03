import numpy as np
from amplify import ConstraintList, Dim2, Model, Poly, PolyArray, one_hot

from config.default import position_cost, position_pair_cost
from constants import ALPHABET_IDX, ALPHABETS, KEY_NUM, KEY_X


class KeyEvalModel(Model):
    def __init__(self, poly_array: PolyArray[Dim2], training_text: str) -> None:
        self.q = poly_array

        char_counts = np.ndarray = np.array([training_text.count(char) for char in ALPHABETS], dtype=np.float64)
        self.char_ratio = np.ndarray = char_counts / char_counts.sum()

        char_pair_counts: np.ndarray[np.float64] = np.zeros(shape=(KEY_NUM, KEY_NUM), dtype=np.float64)
        for i in range(len(training_text) - 1):
            if training_text[i] in ALPHABETS and training_text[i + 1] in ALPHABETS:
                char_pair_counts[ALPHABET_IDX[training_text[i]]][ALPHABET_IDX[training_text[i + 1]]] += 1
        self.char_pair_ratio: np.ndarray[np.float64] = char_pair_counts / sum(char_pair_counts.flatten())

        objectives: Poly = (
            0.2 * self.position_objective()
            + 0.2 * self.position_pair_objective()
            + 0.1 * self.ctrl_objective()
            + 0.1 * self.comma_period_objective()
            + 0.1 * self.vim_objective()
        )
        constraints: ConstraintList = self.position_constraint() + self.key_constraint()
        super().__init__(objective=objectives, constraint=constraints)

    def position_constraint(self) -> ConstraintList:
        """Each key shall be assigned to exactly one position"""
        constraints = ConstraintList()
        for i in range(KEY_NUM):
            char: str = ALPHABETS[i]
            constraints += one_hot(self.q[i, :].sum(), f"{char}th row")
        return constraints

    def key_constraint(self) -> ConstraintList:
        """Each position shall be assigned to exactly one key"""
        constraints = ConstraintList()
        for i in range(KEY_NUM):
            constraints += one_hot(self.q[:, i].sum(), f"{i}th column")
        return constraints

    def position_objective(self) -> Poly:
        return np.einsum(
            "n,cn,c->",
            position_cost,
            self.q,
            self.char_ratio,
        )

    def position_pair_objective(self) -> Poly:
        return np.einsum("ij,ci,dj,cd->", position_pair_cost, self.q, self.q, self.char_pair_ratio)

    def left_right_diff_objective(self) -> Poly:
        f_left = self.char_ratio @ (
            self.q[:, 0:5].sum(axis=1) + self.q[:, 10:15].sum(axis=1) + self.q[:, 20:25].sum(axis=1)
        )
        f_right = self.char_ratio @ (
            self.q[:, 5:10].sum(axis=1) + self.q[:, 15:20].sum(axis=1) + self.q[:, 25:30].sum(axis=1)
        )
        return -((f_left - f_right) ** 2)

    def ctrl_objective(self) -> Poly:
        ctrl_alphabets = ("a", "s", "d", "f", "x", "c", "v")
        return sum(
            (
                self.q[ALPHABET_IDX[char], 0:4].sum()
                + self.q[ALPHABET_IDX[char], 10:14].sum()
                + self.q[ALPHABET_IDX[char], 20:24].sum()
                - 1
            )
            ** 2
            for char in ctrl_alphabets
        )

    def comma_period_objective(self) -> Poly:
        return -sum(
            self.q[ALPHABET_IDX[","], n] * self.q[ALPHABET_IDX["."], n + 1]
            for n in range(KEY_NUM - 1)
            if (n + 1) % KEY_X != 0
        )

    def vim_objective(self) -> Poly:
        return -sum(
            self.q[ALPHABET_IDX["h"], n - 1]
            * self.q[ALPHABET_IDX["j"], n - 10]
            * self.q[ALPHABET_IDX["k"], n]
            * self.q[ALPHABET_IDX["l"], n + 1]
            for n in [11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 27, 28]
        )
