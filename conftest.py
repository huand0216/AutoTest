#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong
import json

from base.method import My_request
import pytest

# 获取租户tenantId
def get_TenantId():
    data = {"account":"A000007","password":"e10adc3949ba59abbe56e057f20f883e"}
    res = My_request().POST(
        url = "http://nursing-test.baisuiyun.com/api/blade-user/getTenantId",
        headers = {"Authorization":"Basic eXljbG91ZDp5eWNsb3VkX3NlY3JldA=="},
        data = data
    )
    return res.json()["data"]["tenantId"]

# 获取护理平台token
@pytest.fixture()
def get_PlatformToken():
    data = {"tenant_id":get_TenantId(),"username":"A000007","password":"e10adc3949ba59abbe56e057f20f883e","scope":"all","type":"account","grant_type":"password"}
    res = My_request().POST(
        url="http://nursing-test.baisuiyun.com/api/blade-auth/oauth/token",
        headers = {"Authorization":"Basic eXljbG91ZDp5eWNsb3VkX3NlY3JldA=="},
        data = data
    )
    token = res.json()["access_token"]
    token_type = res.json()["token_type"]
    return "{0} {1}".format(token_type,token)




