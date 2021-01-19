#本文件用以实现题目的录入和保存
#题库的载入格式是excel格式

import xlrd




#信息载入函数，用来导入excel中的题目信息，导入的内容包括题目类型、题目主干、题目选项、题目答案、题目难度;这里同样需要得到总行数，以计算题目的总数；
#注意单选和多选需要分开储存；

def import_excel(excel_file):
    data = xlrd.open_workbook(excel_file)
    table = data.sheet_by_index(0)
    single_tables=[]
    single_number=0
    multi_tables=[]
    multi_number=0
    for rown in range(table.nrows):
        array = {'question_type':'','question':'','question_choice':'','question_answer':'','question_diffculty':''}
        array['question_type'] = table.cell_value(rown,0)
        array['question'] = table.cell_value(rown,1)
        array['question_choice'] = table.cell_value(rown,2)
        array['question_answer'] = table.cell_value(rown,3)
        array['question_diffculty'] = table.cell_value(rown,5)
        if table.cell_value(rown,0) == '单选题':
            single_tables.append(array)
            single_number++
        if table.cell_value(rown,0) == '多选题':
            multi_tables.append(array)
            multi_number++
    return single_tables,multi_tables,single_number,multi_number

