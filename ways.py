# -*- coding:utf-8 -*-

def how_many_ways(num):
    list_num = str(abs(num))
    """至少一种"""
    count = 1
    if 9 < num < 27:
        count += 1
    elif len(str(num)) > 1:
        for i in range(len(list_num)):
            if 9 < int(list_num[i:i + 2]) < 27:
                count += 1
    return count

print(how_many_ways(19))
