
import os
from pathlib import Path

PROJECT_ROOT: Path = (Path(os.path.realpath(__file__)).resolve().parent / "..").resolve()
PATH_CARD_INFO: Path = PROJECT_ROOT / "assets/card_info"


def purge_directory(path: Path) -> None:
	print(f"Purging folder '{path}'...")
	for file in path.iterdir():
		if file.is_file:
			# print(f"rm {file}")
			file.unlink()

def write_card(suite:str, value:str) -> None:
	card_name: str = f"{suite}_{value}"
	print(f"{card_name}...  \t", end="")

	card_data: str = f"""\
{{
	"name": "{card_name}",
	"front_image": "{card_name}.png",
	"suit": "{suite}",
	"value": "{value}"
}}
"""

	filename: Path = PATH_CARD_INFO / f"{card_name}.json"
	print(filename)
	with open(filename, "w") as file:
		file.write(card_data)
		file.close()
	

def generate_cards() -> int:
	CARD_SUITES: list[str] = ["club", "diamond", "heart", "spade"]
	CARD_VALUES: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

	num_cards: int = 0
	for suite in CARD_SUITES:
		for value in CARD_VALUES:
			write_card(suite, value)
			num_cards += 1

	return num_cards
			

def main():

	print(f"  PROJECT_ROOT='{PROJECT_ROOT}'")
	print(f"PATH_CARD_INFO='{PATH_CARD_INFO}'")
	print()

	purge_directory(PATH_CARD_INFO)
	print()

	generate_cards()

	#write_card("suite", "value")

			


if __name__ == "__main__":
	main()
