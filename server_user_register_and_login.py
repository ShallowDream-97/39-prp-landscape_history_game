#本文件用以实现用户的注册和登陆
import socket
#getID函数用以实现得到用户的IP和PORT

usr_list = {}

#后台存储一个usr_list字典，该字典的格式是存储用户的用户名和ip信息

def usr_msg_receive():
    udp_socket_msg_recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket_msg_recv.bind(("",3344))
    recv_data = udp_socket_msg_recv.recvfrom(1024)
    usr_name = recv_data[0].decode("utf-8")
    usr_ip = recv_data[1].decode("utf-8")
    add_usr(usr_name,usr_ip)

#函数usr_update能够实现用户信息的添加和更新，如果用户是第一次登陆，则直接添加key是用户名的信息，如果不是，则更新
def add_usr(usr,ip):
    global usr_list
    usr_list[usr] = ip



#用于给其他函数读取指定usr的ip信息
def getID(usr):
    global usr_list
    return usr_list[usr]


