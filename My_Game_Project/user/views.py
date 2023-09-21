import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.

def test(request):
    return HttpResponse("测试user")


def check_number(password):
    for c in password:
        if c.isnumeric():
            return True


def check_letter(password):
    for c in password:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            return True


def check_legal(password):
    if len(password) < 8 or len(password) > 16:
        return {'result': 0, 'message': '长度需为8-16个字符,请重新输入。'}
    else:
        for i in password:
            if 0x4e00 <= ord(i) <= 0x9fa5 or ord(i) == 0x20:  # Ox4e00等十六进制数分别为中文字符和空格的Unicode编码
                return {'result': 0, 'message': '不能使用空格、中文，请重新输入。'}
        else:
            key = 0
            key += 1 if check_number(password) else 0
            key += 1 if check_letter(password) else 0
            key += 1 if check_mark(password) else 0
            if key >= 2:
                return {'result': 1, 'message': '密码强度合适'}
            else:
                return {'result': 0, 'message': '至少含数字/字母/字符2种组合，请重新输入。'}


def check_mark(password):
    for c in password:
        if not (c.isnumeric() or 'a' <= c <= 'z' or 'A' <= c <= 'Z'):
            return True


def register(request):
    """
    :param request: 请求体
    :return:    1 - 成功    0 - 失败

    请求体包含 username, password1, password2, email
    """
    if request.method == 'POST':
        result = {'result': 0, 'message': r'正在内测中，暂时不对外开放注册！'}

        data_json = json.loads(request.body.decode())
        print(data_json)

        username = data_json.get('username', '')
        password1 = data_json.get('password1', '')
        password2 = data_json.get('password2', '')
        email = data_json.get('email', '')

        if len(username) == 0 or len(password1) == 0 or len(password2) == 0 or len(email) == 0:
            result = {'result': 0, 'message': '用户名, 密码, 与邮箱不允许为空！'}
            return JsonResponse(result)

        if password1 != password2:
            result = {'result': 0, 'message': r'两次密码不一致!'}
            return JsonResponse(result)

        message = check_legal(password1)

        if message['result'] != 1:
            return JsonResponse(message)
