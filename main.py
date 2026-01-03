import argparse


def main():
    parser = argparse.ArgumentParser(description="Dice roller")
    parser.add_argument(
        "dice_to_roll", type=str, help="Dices to roll in (number)d(sides) notation"
    )


if __name__ == "__main__":
    main()
