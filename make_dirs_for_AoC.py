"""
This script check if you are ready for Advent of Code. In case, you have no day folders (eg. 01, 02, ..)
in current year folder (eg. 2022/) created, it gives you an option to do so.

1.  Clone this script in folder where you like to have the empty files created in structure eg. ./2022/01/01.py
2.  Modify the constant variables such as YEAR, PATH, and FILE_TYPE
3.  Run the script and follow the instructions in your terminal.
"""

import os
import datetime


YEAR = datetime.datetime.today().strftime('%Y')
PATH = 'advent_of_code' # os.path.abspath(os.getcwd())
FILE_TYPE = '.py'


def get_path_with_year(current_year=YEAR, current_path=PATH):
    year_path = os.path.join(current_path, current_year)
    return year_path


def check_folder(path=get_path_with_year(),
                 create_folders=False,
                 create_input_files=False,
                 create_code_files=False,
                 create_input_test_files=False
                 ):
    flag = True
    new_folders = []
    for folder in range(1, 26):
        if folder < 10:
            new_folders.append("0" + str(folder))
        else:
            new_folders.append(str(folder))

    for new_folder in new_folders:
        new_path = os.path.join(path, new_folder)
        new_path_input = os.path.join(new_path, 'input.txt')
        new_path_input_test = os.path.join(new_path, 'input.txt')
        new_path_code = os.path.join(new_path, new_folder + FILE_TYPE)

        if not os.path.exists(new_path):
            print(
                "Folder does not exist: "
                + new_path
                + " -> lets create one to get ready for AoC"
            )
            flag = False
            if create_folders: # to get folders
                os.makedirs(new_path)
                print(
                    new_path + "-> WAS CREATED.",
                )
        elif not create_input_files or not create_code_files:
            print("Folder exists: " + new_path + " -> no need to make a new one.")
        if create_input_files:
            try:
                with open(new_path_input, "x") as input_file: input_file.write('')
                print(f"{new_path_input} -> WAS CREATED.")
            except:
                print(f"{new_path_input} -> WAS NOT CREATED.")
        if create_code_files:
            try:
                with open(new_path_code, "x") as code_file: code_file.write('')
                print(f"{new_path_code} -> WAS CREATED.")
            except:
                print(f"{new_path_code} -> WAS NOT CREATED.")
        if create_input_test_files:
            try:
                with open(new_path_input_test, "x") as input_test_file: input_test_file.write('')
                print(f"{new_path_input_test} -> WAS CREATED.")
            except:
                print(f"{new_path_input_test} -> WAS NOT CREATED.")

    return flag


if __name__ == "__main__":
    all_folders_created = check_folder()
    if all_folders_created:
        print("Your folders are ready for AoC!")
    elif (input("Do you want to create the folders? ('F' for create Folders)\n> ").upper().strip() == "F"):
        check_folder(create_folders=True)
    all_folders_created = check_folder()
    if all_folders_created:
        if (input(f"Do you want to create the {YEAR}/01{FILE_TYPE} an so on files in your folders? ('C' for create Code)\n> ").upper().strip() == "C"):
            check_folder(create_code_files=True)
        if (input("Do you want to create the input.txt files in folders? ('D' for create Data)\n> ").upper().strip() == "D"):
            check_folder(create_input_files=True)
        if (input("Do you want to create the input_test.txt files in folders? ('T' for create Data)\n> ").upper().strip() == "T"):
            check_folder(create_input_test_files=True)

