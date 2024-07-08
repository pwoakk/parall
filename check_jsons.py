import os


def check_files_exist():
    files = ['characteristics.json', 'statistics.json']
    all_exist = True

    for file in files:
        if os.path.exists(file):
            print(f"File {file} exists.")
        else:
            print(f"File {file} does not exist.")
            all_exist = False

    if all_exist:
        print("All files exist.")
    else:
        print("Some files are missing.")


check_files_exist()
