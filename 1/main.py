import os
import shutil


def show_files():
    print(f"Path:{os.getcwd()}\nFiles in directory:\n")
    for element in os.listdir(os.getcwd()):
        print(element)


def change_directory():
    print("ALERT!\nEnter full path to your directory\n")
    path = input("Enter path:\n")
    try:
        os.chdir(path)
    except Exception:
        print("Check that you enter path correct\n")


def copy_files():
    show_files()
    temp = input("What you want to copy\n1 - file\n2 - group of file\n")
    if temp == "1":
        try:
            filename = input("Enter name of file:\n")
            path = input("Enter path where you want to copy:\n")
            shutil.copy(filename, path)
        except FileNotFoundError:
            print("Check that you enter filename correct")
    elif temp == "2":
        try:
            filename = input('Enter files separated by spaces:\n')
            path = input("Enter path where you want to copy:\n")
            for elem in filename.split(" "):
                shutil.copy(elem, path)
        except PermissionError:
            print("Check that you enter files, not directory")
        except FileNotFoundError:
            print("Check that you enter filename correct")
    else:
        print("Чел ты")


while True:
    action = input("Enter your command:\n1 - Show all files in directory\n2 - Change directory\n3 - Copy files\n"
                   "4 - exit.\n")
    if action == "1":
        show_files()
    elif action == "2":
        change_directory()
    elif action == "3":
        copy_files()
    elif action == "4":
        break
    else:
        print("Check correct input")
    print("_____________________")
