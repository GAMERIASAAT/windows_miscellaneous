import os
import subprocess

def create_windows_service(service_name, executable_path):
    """
    Create a Windows service that runs a specific executable on boot.

    Args:
        service_name (str): The name of the service to create.
        executable_path (str): The path to the executable to run.

    Returns:
        None
    """
    # Create the service
    subprocess.run(f"sc create {service_name} binPath= \"{executable_path}\" start= auto", shell=True, check=True)

    # Start the service
    subprocess.run(f"sc start {service_name}", shell=True, check=True)

"""To use this function, simply call it with the name you want to give the service and the path to the executable you want to run:
  service_name = "MyService"
  executable_path = "C:\\path\\to\\my\\executable.exe"

  create_windows_service(service_name, executable_path)

"""
