#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

from base.method import My_request
from common.public_path import get_filePath
import xlrd

'''
操作Excel的工具类
'''
class OperationExcel(object):

    caseId = "caseId"
    remarks = "描述信息"
    url = "url"
    method = "请求方法"
    parameter = "请求参数"
    expect = "预期结果"

    # 添加构造方法
    def __init__(self,dirName,fileName,sheetName):
        '''
        :param dirName: Excel文件目录
        :param fileName: Excel文件名
        :param sheetName: sheet名称
        '''
        self.dirName = dirName
        self.fileName = fileName
        self.sheetName = sheetName
    # 获取sheet
    @property
    def get_Sheet(self):
        book = xlrd.open_workbook(filename=get_filePath(dirName="data",fileName="data.xls"))
        return book.sheet_by_name(self.sheetName)

    # 获取Excel内有效行数
    def valid_raws(self):
        return self.get_Sheet.nrows

    # 获取Excel内有效行数
    def valid_column(self):
        return self.get_Sheet.ncols

    # 获取Excel内的数据并返回列表
    def get_ExcelData(self):
        data = list()
        excel_Key = self.get_Sheet.row_values(rowx=0)
        for i in range(1,self.valid_raws()):
            value = self.get_Sheet.row_values(i)
            result = dict(zip(excel_Key,value))
            data.append(result)
        return data


if __name__ == '__main__':
    obj = OperationExcel(dirName="data",fileName="data.xls",sheetName="data")
    result = obj.get_ExcelData()
    print(result)

