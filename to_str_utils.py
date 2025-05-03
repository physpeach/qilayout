def keylayout_to_str(keylayout: list[list[str]]) -> str:
    """
    Convert a 2D array of key layout to a string representation.
    Args:
        keylayout (list | tuple): 2D array of key layout, where each element is a string.
    Returns:
        str: String representation of the key layout.
    """
    # convert to strings like:
    # | q | w | e | r | t | y | u | i | o | p |
    # | a | s | d | f | g | h | j | k | l | ; |
    # | z | x | c | v | b | n | m | , | . | - |
    return "\n".join(["| " + " | ".join(row) + " |" for row in keylayout])


if __name__ == "__main__":
    # Example usage
    keylayout = [
        ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
        ["z", "x", "c", "v", "b", "n", "m", ",", ".", "-"],
    ]
    print(keylayout_to_str(keylayout))
