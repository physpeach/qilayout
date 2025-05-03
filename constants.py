# key layout
# | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |
# | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
# | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |
KEY_X: int = 10
KEY_Y: int = 3
KEY_NUM: int = KEY_X * KEY_Y

ALPHABETS: str = "abcdefghijklmnopqrstuvwxyz,.-;"
ALPHABET_IDX: dict[int, str] = {i: c for c, i in enumerate(ALPHABETS)}
