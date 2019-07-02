# 中间件文件
from .models import User


def front_user_middleware(get_response):
    # 首先执行初始化代码
    print("11111111")

    def middleware(request):
        print("2222222")
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = get_response(request)
        print("33333333")
        return response

    return middleware


class FrontUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print("11111111")

    def __call__(self, request):
        print("2222222")
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = self.get_response(request)
        print("33333333")
        return response
