def whos_first(p1: str, p2: str) -> str:
    """
    Determine who shot first based on the position of the word 'Bang' in each string.

    Args:
        p1 (str): Player 1's string.
        p2 (str): Player 2's string.

    Returns:
        str: 'p1' if Player 1 shot first,
             'p2' if Player 2 shot first,
             'tie' if both shot at the same time,
             'no shot' if one or both never shot.
    """
    p1_time = p1.find('Bang')
    p2_time = p2.find('Bang')

    if p1_time < 0 or p2_time < 0:
        return "no shot"
    elif p1_time < p2_time:
        return "p1"
    elif p2_time < p1_time:
        return "p2"
    else:
        return "tie"


if __name__ == "__main__":
    print("🔫 Who Shot First? Game")
    print("Type the moment when your shot happens. Use spaces before 'Bang' to delay your shot.\n")

    # Input from players
    p1_input = input("Player 1, enter your shot: ")
    p2_input = input("Player 2, enter your shot: ")

    result = whos_first(p1_input, p2_input)

    if result == "p1":
        print("💥 Player 1 shot first!")
    elif result == "p2":
        print("💥 Player 2 shot first!")
    elif result == "tie":
        print("🤝 It's a tie! Both shot at the same time!")
    else:
        print("😶 No shots fired...")

