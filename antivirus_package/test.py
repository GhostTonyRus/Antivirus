import hashlib

def md5_hash(filename):
    with open(filename, "rb") as file:
        bytes = file.read()
        md5_hash = hashlib.md5(bytes).hexdigest()

    return md5_hash

# print(md5_hash("hosts.txt"))

def malware_checker(pathOfFile):
    hash_malware_check = md5_hash(pathOfFile)
    malware_hashes = open("virus.txt", "r")
    malware_hashes_read = malware_hashes.read().splitlines()
    malware_hashes.close()

    for check in malware_hashes_read:
        if check == hash_malware_check:
            return "red"
        else:
            return "green"


print(md5_hash("hosts.txt"))
# print(malware_checker("hosts.txt"))
def test(file_hash):
    with open("virus_hash.txt", "r") as file:
        hashes = file.readlines()
        for hash in hashes:
            hash_split = hash.split()
            for item in hash_split:
                if file_hash == item:
                    return True
                else:
                    return False

h = md5_hash("hosts.txt")
print(test(h))


