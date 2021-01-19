#本文件用于实现接收服务端发送的题目信息并显示

import socket

def client_question_recv():
    """接收消息"""
    """client_recv用于实现用户端对服务端的全时监听"""
    udp_socket_question_recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket_question_recv.bind(("",7788))
    recv_data = udp_socket_question_recv.recvfrom(1024)
    print(recv_data[0].decode("utf-8"))
