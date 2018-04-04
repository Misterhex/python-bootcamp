from multiprocessing import Pool
import socket

print("-" * 20)
#hostname = raw_input("\nplease enter hostname to scan...\n")
hostname = "jialong-renovation.sg"

print("looking up {}".format(hostname))

ipaddr = socket.gethostbyname(hostname)

print(ipaddr)

def scan(port):
    try:
        print("scanning port {} ...".format(port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ipaddr, port))
        if result == 0:
            print("port {} is open".format(port))
    finally:
        sock.close()

pool = Pool(50)
pool.map(scan, range(1, 1025))

print("-" * 8 + " Completed " + "-" * 8)