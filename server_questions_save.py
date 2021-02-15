#本文件用以实现题目的录入和保存
#题库的载入格式是excel格式

import xlrd         #读excel模块




#信息载入函数，用来导入excel中的题目信息，导入的内容包括题目类型、题目主干、题目选项、题目答案、题目难度;这里同样需要得到总行数，以计算题目的总数；
#注意单选和多选需要分开储存；

def import_excel(excel_file):                       #函数定义
    data = xlrd.open_workbook(excel_file)           #打开excel_file读取数据
    table = data.sheet_by_index(0)                  #通过索引顺序获取excel_file里的一个工作表
    single_tables=[]                                #单选题列表
    single_number=0                                 #单选题数目
    multi_tables=[]                                 #多选题列表
    multi_number=0                                  #多选题数目
    for rown in range(table.nrows):#table.nrows   获取excel_file中的有效行数
        array = {'question_type':'','question':'','question_choice':'','question_answer':'','question_diffculty':''}#创建一个问题词典，包括问题类型，问腿本身，问题选项，问题答案，问题困难程度，是否加问题分值
        array['question_type'] = table.cell_value(rown,0)#返回单元格数据table.cell_value(行值，列值）
        array['question'] = table.cell_value(rown,1)
        array['question_choice'] = table.cell_value(rown,2)
        array['question_answer'] = table.cell_value(rown,3)
        array['question_diffculty'] = table.cell_value(rown,5)
        if table.cell_value(rown,0) == '单选题':
            single_tables.append(array)      #把单选题写入到sing_tables
            single_number+=1                  
        if table.cell_value(rown,0) == '多选题':
            multi_tables.append(array)
            multi_number+=1
    return single_tables,multi_tables,single_number,multi_number

