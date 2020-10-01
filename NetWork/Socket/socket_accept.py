import socket

"""
接收udp数据
# 创建套接字
# 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
# 绑定数据,参数:接收的最大字节
# 打印接收到的数据
# 关闭套接字

端口绑定的问题:动态端口,没指定端口时,默认端口
"""


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    local_address = ("192.168.31.47", 8080)
    udp_socket.bind(local_address)
    # 绑定数据,参数:接收的最大字节
    receive_data = udp_socket.recvfrom(1024)  # 接收的是一个元组(接收到的数据,(发送方的ip,port))
    # 分离获取的数据
    receive_msg = receive_data[0]
    receive_address = receive_data[1]
    # 打印接收到的数据
    # print(receive_data)
    print("address: %s\r\nmsg: %s" % (str(receive_address), receive_msg.decode("UTF-8")))
    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    while True:
        main()
