import argparse

# Read token file
parser = argparse.ArgumentParser(description="Find the best key layout")
parser.add_argument("--english_file", type=str, default="english.txt", help="English file name")
parser.add_argument("--learning_file", type=str, default="learning_english.txt", help="learning file name")

args = parser.parse_args()

try:
    with open(args.english_file) as f:
        data: str = f.read().strip()
except FileNotFoundError:
    print(f"English file: {args.english_file} not found.")
    exit(1)

# pre-process
data = (
    data.replace("\n", " ")
    .replace("!", ".")
    .replace("?", ".")
    .replace(". ", ".")
    .replace(", ", ",")
    .replace(",", ", ")
    .replace(".", ". ")
    .lower()
    .replace(":", ";")
    .replace("<", ",")
    .replace(">", ".")
    .replace("_", "-")
)

while "  " in data:
    data = data.replace("  ", " ")

charactors_for_learning = set("abcdefghijklmnopqrstuvwxyz,.-; ")

# Convert learning_data to roman
for char in data:
    if char not in charactors_for_learning:
        print(f"Unknown character: {char}")
        data = data.replace(char, " ")

# Write to file

print(f"Write to {args.learning_file}, length: {len(data)}")
with open(args.learning_file, "w") as f:
    f.write(data)
