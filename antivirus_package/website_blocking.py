import time

# hosts = "C\\Windows\\System32\\drivers\\etc\\hosts"
hosts = "hosts.txt"

redirect_url = "127.0.0.1"

response = input("Введите url-адрес сайта для блокирвоки:\n>>>")

blocked_sites = []
blocked_sites.append(response)

try:
    with open(hosts, "r+") as file:
        src = file.readlines()
        for site in blocked_sites:
            if site in src:
                print("Сайт уже заблокирвоан!")
            else:
                file.write(f"{redirect_url} {site}\n")
                print("Сайт заблокирован!")
except FileExistsError as err:
    print(err)
site_name = "127.0.0.1 www"
try:
    with open(hosts, "r+") as file:
        src = file.readlines()
        print(src)
        if site_name in src:
            src.remove(site)
            print("Сайт разблокирован!")
        else:
            print("Данный сайт ещё не заблокирован!")
except FileExistsError as err:
    print(err)

