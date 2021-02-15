#The file is used for user to register or login to server.
#The file provided that the client send their name and ip to server
import socket
import client_get_host

def get_usr_id():       #得到用户名，返回两行数据，第一行数据是学号，第二行是用户所用客户端ip，以此标识用户
    usr_id = input("Please input your student id:") #输入学号
    usr_name=input("Please input your usr name:")#输入名字
    usr_ip = client_get_host.get_host_ip()#获取用户IP
    print("Hi,%s!Welcome to run this program",usr_name)
    usr_msg = usr_id+'\n'+usr_ip      #用ip和学号标识用户
    return usr_msg

#In our program, register equals login,so we use server_register_host to receiver all msg.
def register_and_login():
    usr_msg = get_usr_id()   #得到用户的信息
    server_register_ip = "59.78.44.125"   #服务器IP
    server_register_port = 3344    #注册端口
    udp_socket_send_usr_msg = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #创建套接字
    #绑定信息
    udp_socket_send_usr_msg.bind(("",4455))    #绑定端口   绑定地址（host,port）到套接字， 在 AF_INET下，以元组（host,port）的形式表示地址。
    udp_socket_send_usr_msg.sendto(usr_msg.encode("utf-8"),(str(server_register_ip),server_register_port)) #发送 UDP 数据，将数据发送到套接字，address 是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
