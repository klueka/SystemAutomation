import os
from functionPage import backupCommand, grabPathExact, grabPathSimple, backupLoop

'''
Backup script to make syncing to network drives easier.
I reccomend tagging directories and folder you want to backup.
These will save to a hidden text file in you user directory.
This text file will save all your preferences are

'''


def grabPathExact():
    '''
    This checks the path
    ''' 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

def grabPathSimple():
    path = os.path.expanduser('~')
    return path

'''
Useless function now
def getUser():
    user = os.path.expanduser('~')
    return user
'''

print("[+]\nHello welcome to my backup program/script\nI got tired of backuping stuff manually and decided this would be easier\n")
option = input("\nSelect a backup option\n[1]Full User Backup (This is everything within the user directory)\n[2]Specific path/folder\n[3]List folder/file backup config\n[+]:")
while option != 'q' and option != 'Q':
    os.system("clear")
    if option == "1":
        backuplist = backupCommand()
        print("This includes the default config \n(For more detail click option 3 on the main menu to list them out.)")
        yORn = input("Would you like to do the backup now?\nHere is the path line " + backuplist + "\nEnter 'y' or 'n'\n[+]:")
        if yORn == 'y' and "Y":
            os.system(backuplist)
        else:
            pass
        

    elif option == "2":
        os.system("clear")
        print("\n\nPlease enter the path you want to add\nThis will keep adding to a text file so feel free to keep entering full absolute paths\nFor example I have a directory called dev, just enter 'dev' and the program will handle the path format\nAutomatically it will include recursion via system commands. If you want just a specific file, please include absolute path.\nThe program will ask the following questions to specify\n")
        print("\nEnter the letter 'q' or 'Q' to quit\n")
        while option != '/q' and option != '/Q':
            user = grabPathSimple()
            option = input("\n[+]: ")
            if option == 'q' and "Q":
                break
            option = "/" + option.strip()
            f = open("Path&Files.txt", "a")
            f.write("\n")
            f.write(str(option))
            f.close()
            f = open("Path&Files.txt", "r")
            print(f.readlines())
            f.close()


    elif option == "3":
        os.system("clear")
        print("Here is the list:")
        f = open("Path&Files.txt", "r")
        print(f.readlines())
        f.close()
    
    option = input("\nSelect a backup option\n[1]Full User Backup (This is everything within the user directory)\n[2]Specific path/folder\n[3]List folder/file backup config\n[+]:")
