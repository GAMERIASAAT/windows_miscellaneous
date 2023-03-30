import winreg
import subprocess
import os

# Specify the location and name of the executable file to be run
executable_path = "C:\\Path\\to\\your\\executable.exe"

# Create a registry key that will run the executable at system startup
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, "MyService", 0, winreg.REG_SZ, executable_path)
winreg.CloseKey(key)

# Install the executable as a service
service_name = "MyService"
service_display_name = "My Service"
service_description = "This is my service description"
service_executable = f'"{executable_path}"'
service_command = f'sc create "{service_name}" binPath={service_executable} DisplayName="{service_display_name}" Description="{service_description}" start=auto'

subprocess.call(service_command, shell=True)

# Start the service
start_command = f'sc start "{service_name}"'
subprocess.call(start_command, shell=True)
