import datetime
import time

import psutil

def cpu():
	cpu = psutil.cpu_count(False)
	cpu_per = int(psutil.cpu_percent(1))
	return cpu_per

def network():
	# network = psutil.net_io_counters()
	network_sent = int(psutil.net_io_counters()[0]/8/1024)
	network_recv = int(psutil.net_io_counters()[1]/8/1024)
	network_info = f"""
					network_sent: {network_sent}kb,
					network_recv: {network_recv}kb,
	"""
	return network_info.replace("\t", "")

def memory():
	mem = psutil.virtual_memory()
	mb = 100 * 1024 * 1024
	print(mem.used)
	print(mem.free)

def disks():
	disk = psutil.disk_partitions()
	print(disk)


def main():
	res = f"""
	процессор: {print(cpu())}\n
	оперативная память: {print(memory())}\n
	сеть: {print(network())}\n
	"""
	return res.replace("\t", "")

# while True:
# 	time.sleep(1)
# 	print(main())

# while True:
# 	time.sleep(1)
# 	disks()

# while True:
# 	for proc in psutil.process_iter():
# 		# print(f"{proc.pid} - {proc.name()} - {proc.status()} - {datetime.datetime.now()}")
# 		with open("test.txt", "a", encoding="utf-8") as file:
# 			with proc.oneshot():
# 				file.write(f"""{proc.name()} - {proc.status()} - {str(psutil.cpu_percent(1))+"%"} - {round(proc.memory_info().rss / 1000000, 1)}МБ - {datetime.datetime.now().strftime('%H:%M:%S %m-%d-%Y')}
# 						""".replace("\t", "").replace("running", "запущено"))

# while True:
# 	time.sleep(1)
# 	print(psutil.net_io_counters())
while True:
	time.sleep(1)
	for i in psutil.net_connections():
		print(i)