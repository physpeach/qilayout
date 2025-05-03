import argparse
import importlib
import os

import amplify
from amplify import Dim2, FixstarsClient, PolyArray, Result, VariableGenerator, solve

from constants import ALPHABETS, KEY_NUM
from to_str_utils import keylayout_to_str

# Check if amplify is installed
print(amplify.__version__)

# Read token file
parser = argparse.ArgumentParser(description="Find the best key layout")
parser.add_argument("--token_path", type=str, default="token.txt", help="token file name")
parser.add_argument("--model_name", type=str, default="default", help="layout file name")
# TODO:
# parser.add_argument("--model_input_path", type=str, default=None, help="")
# parser.add_argument("--model_output_path", type=str, default=None, help="")

args = parser.parse_args()
try:
    with open(args.token_path) as f:
        TOKEN: str = f.read().strip()
except FileNotFoundError:
    print(f"Token file {args.token_path} not found.")
    exit(1)

training_text = ""
with open("data/English/learning_english.txt") as file:
    training_text += file.read()

with open("data/Japanese/roman.txt") as file:
    training_text += file.read()

# define the 2d array
#       || 00 | 01 | ... | 10 | 11 | ... | 28 | 29 |
# ------||------------------------------------------
# a:  0 ||  0 |  0 | ... | 1? |  0 | ...
# b:  1 || 1? |  0 | ... |  0 |  0 | ...
# ...   ||
# z: 25 ||
# ,: 26 ||
# .: 27 ||
# -: 28 ||
# ;: 29 ||

# q[${Alphabet_ID}, ${Key_ID}]

q: PolyArray[Dim2] = VariableGenerator().array("Binary", (KEY_NUM, KEY_NUM))

# import model dynamically
model_lib = importlib.import_module(f"model.{args.model_name}")
model = model_lib.KeyEvalModel(q, training_text)

print(f"Model:\n{model}")

def qubo_result_to_keylayout(result) -> list[list[str]]:
    """Convert the QUBO result to a key layout string.

    Args:
        result (list): 2D array of QUBO result.

    Returns:
        str: String representation of the key layout.
    """
    keylayout = []
    for j in range(KEY_NUM):
        for i in range(KEY_NUM):
            if result[i][j] == 1.0:
                keylayout.append(ALPHABETS[i])

    # 30 columns to 3 rows * 10 columns
    return [keylayout[i * 10 : i * 10 + 10] for i in range(3)]


client = FixstarsClient()
client.token = TOKEN
client.parameters.timeout = 100 * 1000  # 100 sec. (maximum time for the free plan)

for i in range(5):
    print(f"{i + 1}th iteration...")
    result: Result = solve(model, client)

    print("solved!")
    print(f"execution time: {result.execution_time}")
    print(f"candidates: {result.num_solves}")
    for s in result.solutions:
        solution: Result.Solution = s
        print(f"\tf    = {solution.objective}")
        print(f"\ttime = {solution.time}")

    solution: Result.Solution = result.best

    print("\nbest solution info:")
    print(f"f    = {solution.objective}")
    print(f"time = {solution.time}")

    solution_values = q.evaluate(solution.values)

    keylayout = qubo_result_to_keylayout(solution_values)
    keylayout_str = keylayout_to_str(keylayout)
    print(keylayout_str)

    dirname: str = f"results/{args.layout_name}"
    os.makedirs(dirname, exist_ok=True)
    with open(f"{dirname}/ite_{i + 1}_f_{solution.objective:.4f}.txt", "w") as f:
        f.write(keylayout_str)
