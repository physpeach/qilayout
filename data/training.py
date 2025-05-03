from constants import ALPHABETS


def get_charactor_count(text: str) -> dict:
    """Get information about the alphabets in the text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary containing the count of each alphabet.
    """
    alphabet_count = dict.fromkeys(ALPHABETS, 0)

    for char in text:
        if char in alphabet_count:
            alphabet_count[char] += 1

    return alphabet_count


if __name__ == "__main__":
    # Example usage

    training_text = ""
    with open("English/learning_english.txt") as file:
        training_text += file.read()

    with open("Japanese/roman.txt") as file:
        training_text += file.read()

    print("Training text length:", len(training_text))
    print("Training text:")
    print(f"\t{training_text[:100]} ...")  # Print first 100 characters
    print(get_charactor_count(training_text))
