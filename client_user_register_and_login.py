#The file is used for user to register or login to server.
#The file provided that the client send their name and ip to server
import socket
import client_get_host

def get_usr_id():
    usr_id = input("Please input your student id:")
    usr_name=input("Please input your usr name:")
    usr_ip = client_get_host.get_host_ip()
    print("Hi,%s!Welcome to run this program",usr_name)
    usr_msg = usr_id+'\n'+usr_ip
    return usr_msg

#In our program, register equals login,so we use server_register_host to receiver all msg.
def register_and_login():
    usr_msg = get_usr_id()
    server_register_ip = "59.78.44.125"
    server_register_port = 3344
    udp_socket_send_usr_msg = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket_send_usr_msg.bind(("",4455))
    udp_socket_send_usr_msg.sendto(usr_msg.encode("utf-8"),(str(server_register_ip),server_register_port))