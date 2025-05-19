from pathlib import Path

directory = Path(input("Input directory: "))
newExtension = input("Input new file extension: ")

for file in directory.iterdir():
    if file.is_file():
        parts = file.name.split(".")
        parts[1] = newExtension
        newName = parts[0] + "." + parts[1]
        newPath = file.with_name(newName)
        file.rename(newPath)
        print(f"Renamed {file} to {newPath}")

input("Press enter to quit: ")