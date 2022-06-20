import wmi

disks = wmi.WMI().Win32_LogicalDisk()

# str(round(int(disk[i].Size) / (1024.0 ** 3))) if disk[i]

info_about_disk = ""
for disk in disks:
    info_about_disk += f"""
    имя диска: {disk.Caption}
    описание: {disk.Description}
    размер: {round(int(disk.Size) / (1024.0 ** 3)) if disk == None else "НЕТ ДАННЫХ"}
    файловая система: {disk.FileSystem if disk.FileSystem != None else "НЕТ ДАННЫХ"}\n"""

print(info_about_disk)

