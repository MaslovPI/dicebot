import argparse
from functions.roll import rollMultipleAccumulate


def main():
    parser = argparse.ArgumentParser(description="Dice roller")
    parser.add_argument(
        "dice_to_roll", type=str, help="Dices to roll in (number)d(sides) notation"
    )
    args = parser.parse_args()
    dice_to_roll = args.dice_to_roll
    dice_info = dice_to_roll.split("d")
    if not len(dice_info) == 2:
        raise ValueError("Incorrect dice info")

    number = int(dice_info[0]) if dice_info[0] else 1
    dimensions = int(dice_info[1])
    result = rollMultipleAccumulate(number, dimensions)
    print(f"{dice_to_roll} roll result: {result}")


if __name__ == "__main__":
    main()
