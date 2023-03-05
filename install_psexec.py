import urllib.request

# Replace this with the direct download link to PsExec
psexec_url = "https://download.sysinternals.com/files/PSTools.zip"

# Download the PsExec ZIP file
urllib.request.urlretrieve(psexec_url, "PSTools.zip")

# Extract the PsExec executable from the ZIP file
import zipfile

with zipfile.ZipFile("PSTools.zip", "r") as zip_ref:
    zip_ref.extract("PsExec.exe", path="C:\\WINDOWS\system32")
