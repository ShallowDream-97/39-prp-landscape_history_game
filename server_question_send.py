#本文件用来处理问题的发送（to client）
import socket
import server_user_register_and_login
import server_user_score
#本文件用以处理服务器端对题目的发送，需要发送的信息包括题目类型、题目主干和题目选项


#question_packing函数用于打包问题为数据包,每次发送只发送一道题目，所以packing函数只负责单一题目的数据包生成
def question_packing(question_num,question_type,question,question_choice):
    send_packing_data = question_num + question_type + '\n' + question + '\n' + question_choice
    return send_packing_data

#单独题目的发送函数
def single_question_send(send_packing_data,send_ip,send_port=7788):
    #创建套接字
    udp_socket_single_question_send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket_single_question_send.bind(("",8899))#所有用户的发送端口均使用此端口
    udp_socket_single_question_send.sendto(send_packing_data.encode("utf-8"),(send_ip,send_port))

#综合题目的发送函数 ：发送时需要给题目加一个编号，当收到对应的编号的反馈时，才会发送下一个问题。
def sum_question_send(send_repo):
    question_num = 1
    tem = question_packing(question_num,send_repo[question_num-1]["question_type"],send_repo[question_num-1]["question"],send_repo[question_num-1]["question_choice"])
    send_ip,send_port = server_user_register_and_login.getID()
    single_question_send(tem,send_ip,send_port)
    question_num += 1
    while question_num<10 :
        if server_user_score.feedback_flag():
            tem = question_packing(question_num,send_repo[question_num-1]["question_type"],send_repo[question_num-1]["question"],send_repo[question_num-1]["question_choice"])
            single_question_send(tem,send_ip,send_port)
    
        