import socket

#the function used for client to get self_host
def get_host_ip():    #获取主机ip
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #创建套接字对象s
        s.connect(('8.8.8.8', 80))   #主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
