from .models import User

def front_user_middleware(get_response):
    def middleware(request):
        #  request到达 view之前的中间件
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
        # response 到达浏览器之前的中间件

        return response
    return middleware