#本文件用已实现题目答案的接受和对错评判

import socket
import server_user_score

# 通信函数，用来接收客户端回传的答案
def server_answer_recv():
    """接收答案"""
    udp_socket_answer_recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket_answer_recv.bind(("",9900))
    recv_answer = udp_socket_answer_recv.recvfrom(1024)
    return(recv_answer.decode("utf-8"))


# 比对函数，用于判断答案的正误;判断一个问题的答案是否正确，需要三个参数：题库、序号、用户答案。题库是用户正在完成的题库
def judge_single_answer(user,user_repo,num,answer):
    if answer == user_repo[num-1]["question_answer"]:
        server_user_score.score_add(user)

#*****************************************************************
def judge_multi_answer(repo,num,answer):
#设计一个函数用来处理多选题目答案，用户回传的多选题答案格式是,用逗号分隔开的不同答案
    return 1