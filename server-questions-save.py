#本文件用以实现题目的录入和保存
#题库的载入格式是excel格式

import xlrd
data = xlrd.open_workbook(r'question_excel.xls')
table = data.sheets()[0]

tables=[]

#信息载入函数，用来导入excel中的题目信息，导入的内容包括题目类型、题目主干、题目选项、题目答案、题目难度
def import_excel(excel):
    for rown in range(excel.nrows):
        array = {'question_type':'','question':'','question_choice':'','question_answer':'','question_diffculty':''}
        array['question_type'] = table.cell_value(rown,0)
        array['question'] = table.cell_value(rown,1)
        array['question_choice'] = table.cell_value(rown,2)
        array['question_answer'] = table.cell_value(rown,3)
        array['question_diffculty'] = table.cell_value(rown,5)
    
    tables.append(array)

