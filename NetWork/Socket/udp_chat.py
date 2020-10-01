import socket

"""
udp聊天器
"""


def send_msg():
    """发送数据"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = input("请输入要发送的内容")
    local_address = ("192.168.31.47", 6666)
    dest_address = ("192.168.31.47", 8888)

    udp_socket.bind(local_address)

    udp_socket.sendto(msg.encode("utf-8"), dest_address)
    udp_socket.close()


def receive_msg():
    """接收数据"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_address = ("192.168.31.47", 8888)
    udp_socket.bind(local_address)
    # 绑定数据,参数:接收的最大字节
    receive_data = udp_socket.recvfrom(1024)  # 接收的是一个元组(接收到的数据,(发送方的ip,port))
    # 分离获取的数据
    receive_msg = receive_data[0]
    receive_address = receive_data[1]
    print("address: %s\r\nmsg: %s" % (str(receive_address), receive_msg.decode("UTF-8")))
    udp_socket.close()


def main():
    send_msg()
    receive_msg()


if __name__ == '__main__':
    main()
