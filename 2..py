import time
import hashlib
import requests
import json

def login_send_post():
    # 参数必须按照url、data顺序传入
    telephone = "chanfei"
    password = "1"
    t = int(time.time())
    password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
    print(password)
    # url = "https://ticketapitest.shomes.cn/-/user/login"
    # 为何是8345
    url2 = "http://106.75.154.221:8345/-/user/login"
    # data = 'username=' + telephone + '&password=' + password + '&timestamp=' + str(t)
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    data = {
        "username": telephone,
        "password": password,
        "timestamp": int(t)
    }
    result = requests.post(url=url2, json=data, headers=headers).json()
    print("查看result", result)
    res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
    print("查看res", res)
    value = json.loads(res)
    key = value['key']
    userID = value['id']
    return key, userID

login_send_post()