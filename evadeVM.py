import wmi
import _winreg as reg
import sys

# Check for common virtualization software
vms = ['VirtualBox', 'VMware', 'QEMU', 'Bochs', 'Xen', 'KVM', 'Hyper-V', 'Parallels']

# Check for virtual hardware identifiers
hids = ['VBOX', 'VMWARE', 'XEN', 'BOCHS', 'QEMU']

# Check for registry keys commonly used by virtualization software
keys = ['HARDWARE\ACPI\DSDT\VBOX__', 'SYSTEM\ControlSet001\Services\vmtools']

# Connect to the WMI service
c = wmi.WMI()

# Check for virtual hardware identifiers
for item in c.Win32_ComputerSystemProduct():
    if any(hid in item.IdentifyingNumber for hid in hids):
        sys.exit()

# Check for common virtualization software
for vm in vms:
    if any(vm in p.Caption for p in c.Win32_Processor()):
        sys.exit()

# Check for registry keys commonly used by virtualization software
for key in keys:
    try:
        k = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key)
        sys.exit()
    except:
        pass
