import time
import jwt


def sign_token(payload, exp=3600 * 24):
    """
    :param payload: 私有声明字典
    :param exp: 过期时间
    :return: 签发的登录令牌
    """
    # 获取当前时间戳，并计算得到该令牌的过期时间(默认过期时间为1天)
    payload['exp'] = time.time() + exp
    # 使用 HS256 算法配合密钥签发登录令牌
    TOKEN_SECRET_KEY = 'SECRET_KEY'
    token = jwt.encode(payload, TOKEN_SECRET_KEY, algorithm='HS256')
    return token
