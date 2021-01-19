#本文件用来生成随机题库，题库根据难度选择生成

#在题库保有函数中，构造了单选题库和多选题库，以及题目总数
#根据这些信息生成针对个人的随机题库

import server_questions_save as sqs

import random
#第一个序号用于生成题目序号的随机数列
def question_repo_create(tables,tables_quantity,repo_quantity):
    repo_number_list = random.sample(range(1, tables_quantity), repo_quantity)  
    return repo_number_list

#利用生成的序号数组，从题库中选出题目
def repo_create(tables,repo_number_list):
    repo = []
    for i in repo_number_list:
        repo.append(tables[i])
    
    return repo

#利用上述函数生成单选题库
def single_repo_create(single_tables,single_tables_number,single_repo_num=6):
    #生成单选题库的题库序号
    single_repo_number_list = question_repo_create(single_tables,single_tables_number,single_repo_num)
    #根据题库序号生成题库
    single_repo = repo_create(single_tables,single_repo_number_list)

    return single_repo

#利用上述函数生成多选题库
def multi_repo_create(multi_tables,multi_tables_number,multi_repo_num=4):
    #生成多选题库的题库序号
    multi_repo_number_list = question_repo_create(multi_tables,multi_tables_number,multi_repo_num)
    #根据题库序号生成题库
    multi_repo = repo_create(multi_tables,multi_repo_number_list)

    return multi_repo

#利用上述函数合成综合题库
def sum_repo_create(single_repo,multi_repo):
    repo = single_repo+multi_repo
    return repo

if __name__ == "__main__":
    excelfile = 'question_excel.xls'
    single_tables,multi_tables,single_tables_number,multi_tables_number = sqs.import_excel(excelfile)
    single_repo = single_repo_create(single_tables,single_tables_number,6)
    multi_repo = multi_repo_create(multi_tables,multi_tables_number)
    repo = sum_repo_create(single_repo,multi_repo)
    print (repo)



    
    

    
    