import wmi

disks = wmi.WMI().Win32_LogicalDisk()
info_about_disk = ""
for disk in disks:
    if disk.Caption == "C:":
        print(True)
    info_about_disk += f"""
    имя диска: {disk.Caption}
    описание: {disk.Description}
    размер: {round(int(disk.Size) / (1024.0 ** 3)) if disk.Size != None else "НЕТ ДАННЫХ!"} GB
    файловая система: {disk.FileSystem if disk.FileSystem != None else "НЕТ ДАННЫХ"}\n"""

print(info_about_disk)