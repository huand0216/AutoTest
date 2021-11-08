# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# # Author:Huandong
#
# values = [['A','1'],['B','2'],['C','3'],['A','4'],['B','5'],['C','6'],['A','1'],['B','1'],['D','3'],['C','1'],
# ['G','0'],['W','3'],['H','1'],['Y','2'],['G','7'],['W','1'],['H','5'],['Y','3']]
#
# letters = list()    # 拿到values里面所有字母组成新列表
# for i in values:
#     letters.append(i[0])
# print("求{0}内相同字母对应ASCII码的和".format(letters))
#
# equal_Letters = list()   # 相同字母组成列表
# count = list()    # 已经对比过得字母索引列表
# for x in range(len(letters)):    # 嵌套两层循环过滤出相同字母存入equal_Letters
#     l = list()
#     for y in range(len(letters)):
#         flag = False
#         for c in count:
#             if c == x:
#                 flag = True
#                 break
#         if flag:
#             break
#         if x == y:
#             l.append(letters[x])
#             continue
#         elif letters[x].__eq__(letters[y]):
#             l.append(letters[y])
#             count.append(y)
#     if len(l) != 0:
#         equal_Letters.append(l)
#
# key = list()   # 去重后的字母列表
# for k in equal_Letters:
#     key.append(k[0])
#
# sumList = list()  #每个字母和的列表
# for a in equal_Letters:
#     s = 0
#     for b in a:
#         s=s+ord(b)
#     sumList.append(s)
#
# letter_sum = dict(zip(key,sumList))
# print("\n"+"结果：{0}".format(letter_sum))
#