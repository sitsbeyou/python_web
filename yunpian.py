__author__ = 'Feng Haoyu'
#-*- coding:utf-8 -*-
# 短信http接口的python代码调用示例
import httplib
import urllib
from random import randint
random_number = randint(100000,999999)
#服务地址
host = "yunpian.com"
#端口号
port = 80
#版本号
version = "v1"
#查账户信息的URI
user_get_uri = "/" + version + "/user/get.json"
#智能匹配模版短信接口的URI
sms_send_uri = "/" + version + "/sms/send.json"
#模板短信接口的URI
sms_tpl_send_uri = "/" + version + "/sms/tpl_send.json"
def get_user_info(apikey):
    """
    取账户信息
    """
    conn = httplib.HTTPConnection(host, port=port)
    conn.request('GET', user_get_uri + "?apikey=" + apikey)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str
def send_sms(apikey, text, mobile):#POST方法调用短信接口发短信
    """
    能用接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def tpl_send_sms(apikey, tpl_id, tpl_value, mobile):#第二种自定义模板，具体选择看个人，都可以使用没问题。

    """
    模板接口发短信
    """
    params = urllib.urlencode({'apikey': apikey, 'tpl_id':tpl_id, 'tpl_value': tpl_value, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=port, timeout=30)
    conn.request("POST", sms_tpl_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str
if __name__ == '__main__':
    apikey = "2144e49f2c6af4d17c1bc145832e4df8"#你申请的apikey
    mobile = "18215565503"#需要发送到的手机号，这个可以让用户填写，从前台表单获得
    text = "您的验证码是"+str(random_number)+"【成都东门】"#中间的数字由后台随机生成，一般为6位数字，后台动态验证。中括号里面的内容为已经审核通过的用户的站点应用名。
#查开发者账户信息
    print(get_user_info(apikey))
#调用智能匹配模版接口发短信
    print(send_sms(apikey, text, mobile))
#调用模板接口发短信
    #tpl_id = 1 #对应的模板内容为：您的验证码是#code#【#company#】
    #tpl_value = '#code#=1234&#company#=成都东门'
    #print(tpl_send_sms(apikey, tpl_id, tpl_value, mobile))
