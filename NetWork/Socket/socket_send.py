import socket

"""
# socket.socket(addressFamily,type)

Address Family: 
    AF_INET：用于Internet进程键访问；
    AF_UNIX：用于一台机器进程间通信
Type：套接字类型
    SOCK_STREAM：流式套接字，主要用于TCP协议
    SOCK_DGRAM：数据报套接字，主要用于UDP协议
    
基本流程
# 创建tcp的套接字---流模式
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 使用套接字收/发数据
# 关闭套接字
s.close()

# 创建tcp的套接字---数据报模式
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 使用套接字收/发数据
# 关闭套接字
s.close()
"""


def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定IP和Port
    udp_socket.bind(("192.168.31.47", 8888))
    # 使用套接字发数据
    # 准备接收方的地址+端口号
    destection_address = ("192.168.31.47", 8080)
    # 发送数据,二进制数据
    # udp_socket.sendto(b"Hello World!", destection_address)
    udp_socket.sendto("Hello World!".encode("UTF-8"), destection_address)
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
