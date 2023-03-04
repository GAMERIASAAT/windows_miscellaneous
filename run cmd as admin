import ctypes
import sys

def is_admin():
    """
    Check if the program is running with administrative privileges.

    Returns:
        bool: True if the program is running as an administrator, False otherwise.
    """
    try:
        # Check if the program is running with administrative privileges
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin(command):
    """
    Run a command as an administrator.

    Args:
        command (str): The command to run.

    Returns:
        None
    """
    # Obtain elevated privileges
    params = (ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
    ShellExecuteEx = ctypes.windll.shell32.ShellExecuteExW
    SEE_MASK_NOCLOSEPROCESS = 0x40
    SEE_MASK_FLAG_NO_UI = 0x400
    SEE_MASK_NOASYNC = 0x1000
    lpVerb = ctypes.c_wchar_p("runas")
    lpFile = ctypes.c_wchar_p("cmd.exe")
    lpParameters = ctypes.c_wchar_p(f"/c {command}")
    lpDirectory = ctypes.c_wchar_p()
    nShow = ctypes.c_int(0)
    executeInfo = ctypes.Structure("SHELLEXECUTEINFOW", params)
    executeInfo.lpVerb = lpVerb
    executeInfo.lpFile = lpFile
    executeInfo.lpParameters = lpParameters
    executeInfo.lpDirectory = lpDirectory
    executeInfo.fMask = SEE_MASK_NOCLOSEPROCESS | SEE_MASK_FLAG_NO_UI | SEE_MASK_NOASYNC
    executeInfo.hwnd = None
    executeInfo.nShow = nShow
    success = ShellExecuteEx(ctypes.byref(executeInfo))

    # Check if the command was run successfully
    if not success:
        print("Error: Failed to obtain elevated privileges.")
        sys.exit(1)

# Command to be run as admin
command = "ipconfig /release"

# Check if the program is running as an administrator
if not is_admin():
    # If not, ask for permission to run as administrator
    run_as_admin(f"python \"{sys.argv[0]}\" \"{command}\"")
else:
    # Otherwise, run the command as administrator
    run_as_admin(command)
