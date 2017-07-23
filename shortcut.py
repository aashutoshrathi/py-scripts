import os, winshell
from win32com.client import Dispatch

desktop = winshell.desktop()
path = os.path.join(desktop, "Media Player Classic.lnk")
target = r"D:\Study\Codes\July 17\Battleship.py"
wDir = r"D:\Study\Codes\July 17"
icon = r"D:\Study\Codes\July 17\Battleship.py"

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()