"""
Scripts written By : Aashutosh Rathi
Credits : Stack Overflow and Me.
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


def find_symbol(path):
    for x in range(len(path)-1):
        if path[x] == "\\":
            result = x
    return result


def make_working_dir(file_path):
    sym = find_symbol(file_path)
    return file_path[:sym]


def make_shortcut(file_path, dir_path, name):
    you = os.getlogin()
    startup = os.path.join('C:\\Users', you, 'AppData', 'Roaming',
                            'Microsoft', 'Windows', 'SendTo')
    name = name + '.lnk'
    path = os.path.join(startup, name)
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = file_path
    shortcut.WorkingDirectory = dir_path
    shortcut.IconLocation = file_path
    shortcut.save()


def main():
    print("\n===== Add Your files or Folders to SendTo in easy way =====")
    you = os.getlogin()
    print('Hey!', you)
    file = input('Path of folder to be added to SendTo : ')
    workingDir = make_working_dir(file)
    file = remove_quotes(file)
    workingDir = remove_quotes(workingDir)
    name = input('Folder Name : ')
    make_shortcut(file, workingDir, name)
    print(name, 'added to SendTo Successfully !!')


if __name__ == '__main__':
    main()
