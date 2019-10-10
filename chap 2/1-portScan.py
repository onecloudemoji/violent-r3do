import sys
import socket
if len(sys.argv) < 3:
	print("USAGE: 1-portScan.py HOST PORT".format(sys.argv[0]))
	sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]
port_int = int(port,10)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((host, port_int))

if result == 0:
	print("Port: " +port+ " is open")
else:
	print("Port: " +port+ " is closed")
