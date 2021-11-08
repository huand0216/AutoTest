#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import os
import sys

# 获取指定文件路径
def get_filePath(dirName,fileName):
    '''
    :param dirName: 文件的上级目录名
    :param fileName: 文件名
    :return: 返回指定文件绝对路径
    '''
    filePath = os.path.join(os.path.dirname(os.path.dirname(__file__)),dirName,fileName)
    return filePath



