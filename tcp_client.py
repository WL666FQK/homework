# Author: 王璐
# Date: 2025/1/1
# Time: 22:59

import socket

def tcp_client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    dest_addr=('192.168.188.1',2000)
    client.connect(dest_addr)
    client.send("1234".encode('utf8'))
    data=client.recv(5)  # 表示接收多少字节的数据
    print(data.decode('utf8'))
    data=client.recv(5)  # 传过来的数据可以分多次接收
    print(data.decode('utf8'))
    client.close()

if __name__ == '__main__':
    tcp_client()