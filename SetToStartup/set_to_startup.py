"""
Scripts written By : Aashutosh Rathi
Credits : Stack Overflow and ↑ .

"""


import os
import time
import winshell
import shutil
from win32com.client import Dispatch


def remove_quotes(string):
    """
    This function is used here to remove quotes from
    paths used in this script.

    :param string: Path with quotes.
    :return: Path without quotes.
    """
    if string.startswith('"'):
        string = string[1:]

    if string.endswith('"'):
        string = string[:-1]
    return string


def make_shortcut(file_path, dir_path, name):
    desktop = winshell.desktop()
    name = name + '.lnk'
    path = os.path.join(desktop, name)
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = file_path
    shortcut.WorkingDirectory = dir_path
    shortcut.IconLocation = file_path
    shortcut.save()


def main():
    print("\n===== Add Your files or Folders to startup in easy way =====")
    desktop = winshell.desktop()
    you = os.getlogin()
    startup = os.path.join('C:\\Users', you, 'AppData', 'Roaming',
                            'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    # print(startup)
    print('Hey!', you)
    file = input('Path of File to be added to startup : ')
    workingDir = input('Path of Directory of that file ( i.e. file path without file) : ')
    file = remove_quotes(file)
    workingDir = remove_quotes(workingDir)

    name = input('Name your Shortcut : ')

    make_shortcut(file, workingDir, name)
    name = name + '.lnk'
    path = os.path.join(desktop, name)
    shutil.move(path, startup)
    print('Added You File to Startup Successfully !!')


if __name__ == '__main__':
    main()
