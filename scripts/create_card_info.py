
import os
from pathlib import Path


def purge_directory(path: Path):
	print(f"Purging folder '{path}'...")
	for file in path.iterdir():
		if file.is_file:
			# print(f"rm {file}")
			file.unlink()
		

def write_cards(path: Path):
	CARD_SUITES: list[str] = ["club", "diamond", "heart", "spade"]
	CARD_VALUES: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

	for suite in CARD_SUITES:
		for value in CARD_VALUES:
			
			card_name: str = f"{suite}_{value}"
			print(f"{card_name}...")

			card_data: str = f"""{{
	"name": "{card_name}",
	"front_image": "{card_name}.png",
	"suit": "{suite}",
	"value": "{value}"
}}
"""

			with open(path / f"{card_name}.json", "w") as file:
				file.write(card_data)
				file.close()

def main():
	PROJECT_ROOT: Path = (Path(os.path.realpath(__file__)).resolve().parent / "..").resolve()
	PATH_CARD_INFO: Path = PROJECT_ROOT / "assets/card_info"

	print(PROJECT_ROOT)
	print(PATH_CARD_INFO)

	purge_directory(PATH_CARD_INFO)

	write_cards(PATH_CARD_INFO)

			


if __name__ == "__main__":
	main()
