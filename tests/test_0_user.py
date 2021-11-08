#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong

import pytest
from base.method import My_request
from utils.operationExcel import OperationExcel
from utils.operationYaml import OperationYaml

class Test_user(object):
    excelData = OperationExcel(dirName="data",fileName="data.xls",sheetName="user_nursing").get_ExcelData()

    @pytest.mark.parametrize(
        "excelData",excelData
    )
    def test_user(self,excelData,get_PlatformToken):
        url = excelData[OperationExcel.url]
        method = excelData[OperationExcel.method]
        remarks = excelData[OperationExcel.remarks]
        request_data = OperationYaml(dirName="data",fileName="data.yaml").get_mappingYaml(excelData[OperationExcel.parameter])
        expect = excelData[OperationExcel.expect]

        print(remarks+" ",end='')

        if method == "POST":
            res = My_request().POST(
                url = url,
                params = request_data,
                headers = {"blade-auth":get_PlatformToken}
            )
            tenantId = res.json()["data"][expect]
            assert tenantId in res.text

        elif method=="GET":
            res = My_request().GET(
                url = url,
                params = request_data,
                headers = {"blade-auth":get_PlatformToken}
            )
            assert expect in res.text

if __name__ == '__main__':
    pytest.main(["-v","-s","test_0_user.py"])