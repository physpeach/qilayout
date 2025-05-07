import argparse

# Read token file
parser = argparse.ArgumentParser(description="Find the best key layout")
parser.add_argument("--hiragana_file", type=str, default="hiragana.txt", help="hiragana file name")
parser.add_argument("--roman_file", type=str, default="roman.txt", help="roman char file name")

args = parser.parse_args()

try:
    with open(args.hiragana_file) as f:
        hiragana: str = f.read().strip()
except FileNotFoundError:
    print(f"Hiragana file: {args.hiragana_file} not found.")
    exit(1)

# pre-process
hiragana = (
    hiragana.replace(" ", "")
    .replace("\n", "")
    .replace("、", "、 ")
    .replace("。", "。 ")
    .replace("?", "。 ")
    .replace("<", "、 ")
    .replace("_", "ー")
)

hiragana_to_roman: dict[str, str] = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
    "さ": "sa",
    "し": "shi",
    "す": "su",
    "せ": "se",
    "そ": "so",
    "た": "ta",
    "ち": "chi",
    "つ": "tsu",
    "て": "te",
    "と": "to",
    "な": "na",
    "に": "ni",
    "ぬ": "nu",
    "ね": "ne",
    "の": "no",
    "は": "ha",
    "ひ": "hi",
    "ふ": "fu",
    "へ": "he",
    "ほ": "ho",
    "ま": "ma",
    "み": "mi",
    "む": "mu",
    "め": "me",
    "も": "mo",
    "や": "ya",
    "ゆ": "yu",
    "よ": "yo",
    "ら": "ra",
    "り": "ri",
    "る": "ru",
    "れ": "re",
    "ろ": "ro",
    "わ": "wa",
    "を": "wo",
    "ん": "xn",
    "が": "ga",
    "ぎ": "gi",
    "ぐ": "gu",
    "げ": "ge",
    "ご": "go",
    "ざ": "za",
    "じ": "ji",
    "ず": "zu",
    "ぜ": "ze",
    "ぞ": "zo",
    "だ": "da",
    "ぢ": "di",
    "づ": "du",
    "で": "de",
    "ど": "do",
    "ば": "ba",
    "び": "bi",
    "ぶ": "bu",
    "べ": "be",
    "ぼ": "bo",
    "ぱ": "pa",
    "ぴ": "pi",
    "ぷ": "pu",
    "ぺ": "pe",
    "ぽ": "po",
    "きゃ": "kya",
    "きゅ": "kyu",
    "きょ": "kyo",
    "しゃ": "sha",
    "しゅ": "shu",
    "しょ": "sho",
    "ちゃ": "cha",
    "ちゅ": "chu",
    "ちょ": "cho",
    "にゃ": "nya",
    "にゅ": "nyu",
    "にょ": "nyo",
    "ひゃ": "hya",
    "ひゅ": "hyu",
    "ひょ": "hyo",
    "みゃ": "mya",
    "みゅ": "myu",
    "みょ": "myo",
    "りゃ": "rya",
    "りゅ": "ryu",
    "りょ": "ryo",
    "ぎゃ": "gya",
    "ぎゅ": "gyu",
    "ぎょ": "gyo",
    "じゃ": "ja",
    "じゅ": "ju",
    "じょ": "jo",
    "ぢゃ": "dya",
    "ぢゅ": "dyu",
    "ぢょ": "dyo",
    "びゃ": "bya",
    "びゅ": "byu",
    "びょ": "byo",
    "ぴゃ": "pya",
    "ぴゅ": "pyu",
    "ぴょ": "pyo",
    "ふぁ": "fa",
    "ふぃ": "fi",
    "ふぇ": "fe",
    "ふぉ": "fo",
    "てぃ": "thi",
    "っ": "",
    "ー": "-",
    "、": ",",
    "。": ".",
    "；": ";",
    "：": ":",
    ":": ":",
}

roman = ""

# Convert hiragana to roman
i: int = 0
while True:
    if i + 1 < len(hiragana) and (hiragana[i] + hiragana[i + 1] in hiragana_to_roman):
        roman += hiragana_to_roman[hiragana[i] + hiragana[i + 1]]
        i += 1
    if hiragana[i] == "っ":
        roman += hiragana_to_roman[hiragana[i+1]][0]
    elif hiragana[i] in hiragana_to_roman:
        roman += hiragana_to_roman[hiragana[i]]
    elif hiragana[i].isalpha():  # Check if the character is an English alphabet
        roman += hiragana[i]
    elif hiragana[i] == " ":
        roman += " "
    else:
        print(f"Unknown character: {hiragana[i]}")

    i += 1
    if not (i < len(hiragana)):
        break

# Write to file

print(f"Write to {args.roman_file}, length: {len(roman)}")
with open(args.roman_file, "w") as f:
    f.write(roman)
