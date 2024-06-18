import os
import time

def grabPathExact():
    '''
    This checks the path
    ''' 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

def grabPathSimple():
    path = os.path.expanduser('~')
    return path


def backupLoop(argc):
    path = str(grabPathSimple()) + str(argc)
    path = path.strip() + "/"
    return path

def backupCommand():
    import time 
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    f = open("Path&Files.txt", "r")
    systemCommand = "zip -r Backup_" + curr_time + ".zip "
    while line := f.readline():
        backup = backupLoop(line)
        systemCommand += backup + " "
    f.close()
    return systemCommand