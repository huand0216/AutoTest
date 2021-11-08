#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong
import errno

import requests
import json

'''
二次封装request请求方法，使请求方法更加简洁
'''
class My_request(object):
    # 通用请求方法
    def my_request(self,url,method,**kwargs):
        try:
            return requests.request(method=method, url=url, **kwargs)
        except BaseException as e:
            print(e.args)

    # GET请求方法
    def GET(self,url,**kwargs):
        try:
            return requests.get(url=url,**kwargs)
        except BaseException as e:
            print(e.args)

    # POST请求方法
    def POST(self,url,**kwargs):
        try:
            return requests.post(url=url,**kwargs)
        except BaseException as e:
            print(e.args)

    # PUT请求方法
    def PUT(self,url,**kwargs):
        try:
            return requests.put(url=url,**kwargs)
        except BaseException as e:
            print(e.args)


if __name__ == '__main__':
    jsonData = {"account":"A210027","password":"had123"}
    headers = {"Authorization":"Basic bWVjaGM6bWVjaGNfc2VjcmV0"}
    obj = My_request().POST(url="http://pxcs.aged.aijk.net/api/blade-user/getTenantId",data=jsonData,headers=headers)
    result = json.dumps(obj.json(),indent=2,ensure_ascii=False)
    print(result)



