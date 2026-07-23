from pathlib import Path

PLACEHOLDER = "[name]"

# Get the folder where main.py is located.
BASE_DIR = Path(__file__).resolve().parent

# Create the complete file paths.
names_path = BASE_DIR / "Input" / "Names" / "invited_names.txt"
letter_path = BASE_DIR / "Input" / "Letters" / "starting_letter.txt"
output_folder = BASE_DIR / "Output" / "ReadyToSend"

# Create the output folder if it does not already exist.
output_folder.mkdir(parents=True, exist_ok=True)

# Read all invited names.
with open(names_path, encoding="utf-8") as names_file:
    names = names_file.readlines()

# Read the starting letter template.
with open(letter_path, encoding="utf-8") as letter_file:
    letter_contents = letter_file.read()

# Create one personalized letter for each name.
for name in names:
    stripped_name = name.strip()

    new_letter = letter_contents.replace(
        PLACEHOLDER,
        stripped_name
    )

    output_path = output_folder / f"letter_for_{stripped_name}.txt"

    with open(output_path, mode="w", encoding="utf-8") as completed_letter:
        completed_letter.write(new_letter)

print("All letters were created successfully.")