# -*- coding: utf-8 -*-
"""
Create on Mon Oct 06 18:26:23 2024
@author: fangg
"""

def replace_function(path):
    a = {
        "打印":"print",
        "输入":"input",
        "真":"True",
        "假":"False",
        "空":"None",
        "非":"not",
        "与":"and",
        "或":"or",
        "重复执行":"for",
        "如果":"if",
        "否则如果":"elif",
        "否则":"else",
        "定义":"def",
        "在":"in",
        "数字迭代器":"range",
        "返回":"return",
        "为":"=",
        "加等于":"+=",
        "取模":"%",
        "加":"+",
        "减":"-",
        "乘":"*",
        "除":"/",
        "设成":"as",
        "断言":"assert",
        "异步执行":"async",
        "异步等待":"await",
        "跳出循环":"break",
        "定义类":"class",
        "下一次":"continue",
        "发生异常":"except",
        "不论如何":"finally",
        "从":"from",
        "导入":"import",
        "全局":"global",
        "完全相同":"is",
        "匿名":"lambda",
        "非局部":"nonlocal",
        "过！":"pass",
        "引发错误":"raise",
        "尝试":"try",
        "如果这样就重复执行":"try",
        "使用":"with",
        "迭代返回":"yield",
        "是否等于":"==",
        "是否不等于":"!="
    }
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        for j in a.keys():
            lines[i] = lines[i].replace(j, a[j])
    with open(path + ".py", "w", encoding="utf-8") as file:
        for i in lines:
            file.write(i)

if __name__ == '__main__':
    path = input("输入文件：")
    replace_function(path)
