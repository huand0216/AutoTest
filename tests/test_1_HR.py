#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import pytest
from base.method import My_request
from utils.operationExcel import OperationExcel
from utils.operationYaml import OperationYaml


'''
测试人力资源的员工信息
'''
class Test_Emp(object):
    excelData = OperationExcel(dirName="data", fileName="data.xls", sheetName="HR_nursing").get_ExcelData()

    def test_addHR(self,get_PlatformToken):
        url = self.excelData[0][OperationExcel.url]
        remark = self.excelData[0][OperationExcel.remarks]
        method = self.excelData[0][OperationExcel.method]
        table = self.excelData[0][OperationExcel.parameter]
        expect = self.excelData[0][OperationExcel.expect]

        params = OperationYaml(fileName="data.yaml").get_mappingYaml(key=table)

        res = My_request().POST(
            headers={"Blade-Auth": get_PlatformToken},
            url = url,
            json = params,
            )
        print(remark+" ",end="")
        assert expect in res.text

    def test_getHR(self,get_PlatformToken):
        url = self.excelData[1][OperationExcel.url]
        remark = self.excelData[1][OperationExcel.remarks]
        method = self.excelData[1][OperationExcel.method]
        table = self.excelData[1][OperationExcel.parameter]
        expect = self.excelData[0][OperationExcel.expect]

        params = OperationYaml(fileName="data.yaml").get_mappingYaml(key=table)

        res = My_request().GET(
            headers = {"Blade-Auth":get_PlatformToken},
            url = url,
            params = params
        )
        # 获取到新增人员的id，更新到删除人员case的参数中
        personId = res.json()["data"]["records"][0]["id"]
        old_Yaml = OperationYaml(fileName="data.yaml").readYaml_dict()
        old_Yaml["case008"]["ids"] = personId
        updateYaml = OperationYaml(fileName="data.yaml").writeYaml(content=old_Yaml)

        print(remark+" ",end="")
        assert expect in res.text

    def test_delHR(self,get_PlatformToken):
        url = self.excelData[2][OperationExcel.url]
        remark = self.excelData[2][OperationExcel.remarks]
        method = self.excelData[2][OperationExcel.method]
        table = self.excelData[2][OperationExcel.parameter]
        expect = self.excelData[2][OperationExcel.expect]

        params = OperationYaml(fileName="data.yaml").get_mappingYaml(key=table)
        # expect = OperationYaml(fileName="temporary.yaml").readYaml_dict()["nursing"]["personId"]
        res = My_request().POST(
            headers = {"Blade-Auth": get_PlatformToken},
            url = url,
            params = params
        )
        print(remark + " ", end="")
        assert expect in res.text

'''
测试人力资源的员工岗位管理
'''
class Test_Emp_position():
    excelData_obj = OperationExcel(fileName="data.xls").get_ExcelData()
    request_obj = My_request()

    def test_addEmp_position(self):
        res = self.request_obj.POST(
        )


if __name__ == '__main__':
    pytest.main(["-v","-s","test_1_HR.py"])
    # obj = Test_human_resources().test_addHR()