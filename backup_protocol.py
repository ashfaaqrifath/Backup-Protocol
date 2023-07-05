import os
import shutil
import time
import colorama
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
sliit_backup = "G:/My Drive/Documents/SLIIT"

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

def progress(percent=0, width=30):
    symbol = width * percent // 100
    blanks = width - symbol
    print('\r[ ', Fore.GREEN + symbol * "█", blanks*' ', ' ]',
          f' {percent:.0f}%', sep='', end='', flush=True)

print()
print(Back.YELLOW + Fore.BLACK + " BACKUP PROTOCOL ")
print(Fore.LIGHTBLACK_EX + "Copyright © 2023 Ashfaaq Rifath")

while True:
    print('''
 (1) Documents
 (2) Pictures
 (3) Videos
 (4) Music
 ''')
    main_option = input(Fore.CYAN + " Select backup object: " + Style.RESET_ALL)

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

    else:
        print(" " + Fore.BLACK  + Back.RED + " INVALID OPTION ")
        print()