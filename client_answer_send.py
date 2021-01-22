#本文件用来采集答案，并发送给服务端

import socket
import client_get_host

#一个简单的输入输出采集函数用来获取答案的字符串格式
def get_answer():
    answer = input("请输入你的答案（使用小写字母，多选请用逗号隔开答案）：")
    return answer


#此函数用来发送答案给服务器
def send_answer(answer):
    server_answer_ip = "59.78.44.125"#目前将服务器部署在宿舍主机上
    server_answer_port = 9900
    udp_socket_send_answer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket_send_answer.bind(("",7911))#所有用户的发送端口均使用此端口
    udp_socket_send_answer.sendto(answer.encode("utf-8"),(server_answer_ip,server_answer_port))ß