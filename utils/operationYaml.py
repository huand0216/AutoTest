#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

from common.public_path import get_filePath
import yaml

class OperationYaml(object):
    # 添加构造方法
    def __init__(self,dirName="data",fileName=None):
        self.dirName=dirName
        self.fileName=fileName

    # 读取yaml文件，返回列表
    def readYaml_list(self):
        f = open(get_filePath(dirName=self.dirName,fileName=self.fileName))
        return list(yaml.safe_load_all(f))

    # 读取yaml文件，返回列表
    def readYaml_dict(self):
        f = open(get_filePath(dirName=self.dirName, fileName=self.fileName))
        return yaml.safe_load(f)

    # 写入/覆盖yaml文件
    def writeYaml(self, content):
        f = open(file=get_filePath(dirName=self.dirName, fileName=self.fileName), mode="w")
        yaml.dump(content, stream=f)

    # 普通文本的读取
    def readText(self):
        f = open(file=get_filePath(dirName=self.dirName,fileName=self.fileName))
        return f.read()

    # 普通文本写入
    def writeText(self,content):
        f = open(file=get_filePath(dirName=self.dirName,fileName=self.fileName),mode="w")
        f.write(content)

    # 获取Excel内参数标识映射的参数
    def get_mappingYaml(self,key):
        if key == "":
            return None
        else:
            return self.readYaml_dict()[key]

if __name__ == '__main__':
    # print(OperationYaml(dirName="data",fileName="data.yaml").readYaml_list())
    data = "测试"
    obj = OperationYaml(dirName="data",fileName="data.yaml")
    print(obj.get_mappingYaml(key="case002"))