#本文件用来保存用户分数、计算得分以及排序并显示最终分数的结果

#本文件提供计算分数的功能函数。
#首先本文件中需要创建一个字典存储每个用户的得分情况，考虑到用户使用的是学号信息，具有唯一性，可以用学号作为key
#需要实现的函数包括分数计算函数（在争上游的demo中只需要实现加分，并且答对每道题只加1分）
#另外本文件中还需要实现一个胜负评判函数、一个计分状态刷新flag函数（用于告知服务器，已经完成一次题目计分，可以发送下一道题目，之所以不放在receive文件中，是考虑到接收和计分完成是两个不同的状态）


#争上游demo情况不考虑多用户情况，所以暂时使用一个固定大小的score_list函数
#def score_list_create ():
usr_score_list = {"twist":0,"fate":0}
#    return user_score_list

def feedback_flag():
    return 1

def score_add(usr:str):
    global usr_score_list
    usr_score_list[usr] += 1

def winner_judge():
    global usr_score_list
    tmp_score = 0
    tmp_winner = "no winner"
    for i in usr_score_list.keys():
        if usr_score_list[i] > tmp_score:
            tmp_winner = i
            tmp_score = usr_score_list[i]
        if usr_score_list[i] == tmp_score:
            tmp_winner = "no winner"
    return tmp_winner