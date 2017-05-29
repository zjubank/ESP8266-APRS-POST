import socket
HOST = '116.236.128.220'
PORT = 14580

while 1:
	msg = input("Please input position:")
	name = msg.split()[0]
	passwd = msg.split()[1]
	pos = msg.split()[2]
	cmd = name+">APRS,TCPIP*:="+pos+"-ESP8266Python"
	login = "user "+name+" pass "+passwd+" vers ESP8266Python 1.0 filter m/2000\r\n"
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((HOST, PORT))
	except OSError:
		print("OSError, check the Internet connection")
		continue
	s.send(login+cmd+"\r\n")
	data = s.recv(1024)
	print(data)
	s.close()
