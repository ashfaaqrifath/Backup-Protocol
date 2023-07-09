import os
import shutil
import time
import subprocess
import colorama
from tqdm import tqdm
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

logos = "C:/Users/ashfa/Pictures/Logos"
logos_backup = "G:/My Drive/Pictures/Logos"

screenshots = "C:/Users/ashfa/Pictures/Screenshots"
screenshots_backup = "G:/My Drive/Pictures/Screenshots"

wallpapers = "C:/Users/ashfa/Pictures/Wallpapers"
wallpapers_backup = "G:/My Drive/Pictures/Wallpapers"

images = "C:/Users/ashfa/Pictures/Images"
images_backup = "G:/My Drive/Pictures/Images"

pics = "C:/Users/ashfa/Pictures/Pics"
pics_backup = "G:/My Drive/Pictures/Pics"

projects = "C:/Users/ashfa/OneDrive/Documents/My Projects"
projects_backup = "G:/My Drive/Documents/My Projects"

portfolio = "C:/Users/ashfa/OneDrive/Documents/Ashfaaq Rifath Portfolio"
portfolio_backup = "G:/My Drive/Documents/Ashfaaq Rifath Portfolio"

sliit = "C:/Users/ashfa/OneDrive/Documents/SLIIT"
sliit_backup = "G:/My Drive/SLIIT"

passwords = "C:/Users/ashfa/OneDrive/Documents/Passwords"
passwords_backup = "G:/My Drive/Documents/Passwords"

videos = "C:/Users/ashfa/Videos"
videos_backup = "G:/My Drive/Videos"

music = "C:/Users/ashfa/Music"
music_backup = "G:/My Drive/Music"

#######################################################################

def folder_backup(src_folder, des_folder):
    if os.path.exists(des_folder):
        shutil.rmtree(des_folder)
    shutil.copytree(src_folder, des_folder)

def folder_comparison(folder1, folder2):
    command = f'robocopy "{folder1}" "{folder2}" /L /E'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        pass
    print(Fore.GREEN + " Displaying folder content comparison")

def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print('\r[ ', Fore.GREEN + symbol * "█", blanks*' ', ' ]',
          f' {percent:.0f}%', sep='', end='', flush=True)

print()
print(Back.YELLOW + Fore.BLACK + " BACKUP PROTOCOL ")
print(Fore.LIGHTBLACK_EX + "Copyright © 2023 Ashfaaq Rifath")

# Below is the real-time progress bar feature

# def count_total_files(folder):
#     total_files = len(os.listdir(folder))
#     return total_files

# def get_files(folder):
#     files = []
#     for file_name in os.listdir(folder):
#         file_path = os.path.join(folder, file_name)
#         if os.path.isfile(file_path):
#             files.append(file_path)
#     return files


# total_files = count_total_files(screenshots) 
# with tqdm(total=total_files, unit="file") as pbar:
#         for fl in screenshots:
#             files = get_files(screenshots)  
#             for file in files:

#                 folder_backup(screenshots, screenshots_backup)
#                 pbar.update(1)

while True:
    print('''
 (1) Documents
 (2) Pictures
 (3) Videos
 (4) Music
 (5) Folder comparison
 ''')
    main_option = input(Fore.CYAN + " Select option: " + Style.RESET_ALL)

    if main_option == "1":
        print('''
 (1) My Projects
 (2) Ashfaaq Rifath Portfolio
 (3) SLIIT
 (4) Passwords
 ''')
        sub_option = input(Fore.CYAN + " Select backup folder: " + Style.RESET_ALL)

        if sub_option == "1":
            print("")
            print(Fore.YELLOW + "     My Projects backup in progress...")
            folder_backup(projects, projects_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

        elif sub_option == "2":
            print("")
            print(Fore.YELLOW + "     Portfolio backup in progress...")
            folder_backup(portfolio, portfolio_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

        elif sub_option == "3":
            print("")
            print(Fore.YELLOW + "     SLIIT backup in progress...")
            folder_backup(sliit, sliit_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

        elif sub_option == "4":
            print("")
            print(Fore.YELLOW + "     Passwords backup in progress...")
            folder_backup(passwords, passwords_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

    elif main_option == "2":
        print('''
 (1) Images
 (2) Screenshots
 (3) Wallpapers
 (4) Pics
 (5) Logos
 ''')
        sub_option = input(Fore.CYAN + " Select backup folder: " + Style.RESET_ALL)

        if sub_option == "1":
            print("")
            print(Fore.YELLOW + "   Images backup in progress...")
            folder_backup(images, images_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

        elif sub_option == "2":
            print("")
            print(Fore.YELLOW + "   Screenshots backup in progress...")
            folder_backup(screenshots, screenshots_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

        elif sub_option == "3":
            print("")
            print(Fore.YELLOW + "   Wallpapers backup in progress...")
            folder_backup(wallpapers, wallpapers_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

        elif sub_option == "4":
            print("")
            print(Fore.YELLOW + "   Pics backup in progress...")
            folder_backup(pics, pics_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

        elif sub_option == "5":
            print("")
            print(Fore.YELLOW + "   Logos backup in progress...")
            folder_backup(logos, logos_backup)
            for i in range(101):
                progress(i)
                time.sleep(0.01)
            print()
            print(Fore.GREEN + "         Backup successful")
            print("")

    elif main_option == "3":
        print("")
        print(Fore.YELLOW + "   Videos backup in progress...")
        folder_backup(videos, videos_backup)
        for i in range(101):
            progress(i)
            time.sleep(0.01)
        print()
        print(Fore.GREEN + "         Backup successful")
        print("")

    elif main_option == "4":
        print("")
        print(Fore.YELLOW + "   Music backup in progress...")
        folder_backup(music, music_backup)
        for i in range(101):
            progress(i)
            time.sleep(0.01)
        print()
        print(Fore.GREEN + "         Backup successful")
        print("")

    elif main_option == "5":
        print('''
 (1) My Projects
 (2) Ashfaaq Rifath Portfolio
 (3) SLIIT
 (4) Passwords
 (5) Images
 (6) Screenshots
 (7) Wallpapers
 (8) Pics
 (9) Logos
 ''')
        sub_option = input(Fore.CYAN + " Select comparison folder: " + Style.RESET_ALL)
        if sub_option == "1":
            folder_comparison(projects, projects_backup)

        elif sub_option == "2":
            folder_comparison(portfolio, portfolio_backup)

        elif sub_option == "3":
            folder_comparison(sliit, sliit_backup)

        elif sub_option == "4":
            folder_comparison(passwords, passwords_backup)

        elif sub_option == "5":
            folder_comparison(images, images_backup)

        elif sub_option == "6":
            folder_comparison(screenshots, screenshots_backup)

        elif sub_option == "7":
            folder_comparison(wallpapers, wallpapers_backup)

        elif sub_option == "8":
            folder_comparison(pics, pics_backup)

        elif sub_option == "9":
            folder_comparison(logos, logos_backup)

    else:
        print(" " + Fore.BLACK  + Back.RED + " INVALID OPTION ")
        print()


# This tool is designed for my use cases only. changes can be made according to your uses.
