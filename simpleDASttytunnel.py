#!/usr/bin/python3
#-*- coding: utf8 -*-
import das

__author__ = 'Olivier Kaufmann'

from settings import LocalHost, LocalPort, EOL, DefaultConnectionDev as comport
import socket
import busconnection as bc
import sys

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket for communication with connecting clients
ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # for socket reuse if interrupted (avoid [Errno 98] Address already in use) TODO : check whether this works...

#comport = '/dev/ttyUSB0'
netid = '255'
serconn = bc.NanoDasConnectionSerial(comport)
LocalSerialDas = das.Das()
LocalSerialDas.connection = serconn
#LocalSerialDas.connect()

print('DAS connected on %s' % comport)

try:
    ServerSocket.bind((LocalHost, LocalPort))
    print('Trying to connect on %s %s' % (LocalHost, LocalPort))

except socket.error as err:
    print('Connection failed : %s' % err)
    sys.exit()

while 1:
    ServerSocket.listen(2)
    print('Server socket is listening...')
    ConnectedClient, address = ServerSocket.accept()
    print('Connected by ', address)
    while 1:
        cmd = ConnectedClient.recv(4)  # receive command from client
        if not cmd:
            break
        check = cmd.decode('ascii').replace('\r','')
        if check != '':
            print('Received command', cmd.decode('ascii'), 'from', address)
            #LocalSerialDas.connection.flushInput() # Empty Das connection output buffer
            LocalSerialDas.connection.write(cmd)  # send command to local Das
        data = LocalSerialDas.connection.read()  # receive data from local Das
        if cmd != b'#XB\r':
            while EOL not in data:
                data += LocalSerialDas.connection.read()  # receive data from remote host
        else:
            while b'\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe' not in data: # generalize for less than 4 channels
                data += LocalSerialDas.connection.read()  # receive data from remote host
        print('Received data from das ', netid, ' on device :', comport)
        print(repr(data))
        ConnectedClient.send(data)  # send data to client
    ConnectedClient.close()

LocalSerialDas.connection.close()