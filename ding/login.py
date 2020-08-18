from django.shortcuts import render,redirect

# 构造钉钉登录url
def ding_url(request):
    appid = 'dingoadwlig6jqq0zddhf0'
    redirect_uri = 'http://localhost:8000/ding/ding_back/'

    return redirect(
        'https://oapi.dingtalk.com/connect/qrconnect?appid=' + appid + '&response_type=code&scope=snsapi_login&state=STATE&redirect_uri=' + redirect_uri)

import requests
import time
import hmac
import base64
from hashlib import sha256
import urllib
import json
from django.http import HttpResponse

#构造钉钉回调方法
def ding_back(request):

    #获取code
    code = request.GET.get("code")

    t = time.time()
    #时间戳
    timestamp = str((int(round(t * 1000))))
    appSecret = 'jj7aAELFmdG3AO4KaNF8cZaE-ZLDFTmVdsJsJKVTdtRqI7biJLtvonkhaOu4hiZO'
    #构造签名
    signature = base64.b64encode(hmac.new(appSecret.encode('utf-8'),timestamp.encode('utf-8'), digestmod=sha256).digest())
    #请求接口，换取钉钉用户名
    payload = {'tmp_auth_code':code}
    headers = {'Content-Type': 'application/json'}
    res = requests.post('https://oapi.dingtalk.com/sns/getuserinfo_bycode?signature='+urllib.parse.quote(signature.decode("utf-8"))+"&timestamp="+timestamp+"&accessKey=dingoadwlig6jqq0zddhf0",data=json.dumps(payload),headers=headers)

    re_dict = json.loads(res.text)
    print(re_dict)

    return HttpResponse(res.text)