from django.http import HttpResponse
from django.shortcuts import redirect

# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         return view_func(request, *args, **kwargs)
#     return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group_list = []
            if request.user.groups.exists():
                for g in request.user.groups.all():
                    group_list.append(g.name)
                for group in group_list:
                    if group in allowed_roles:
                        return view_func(request, *args, **kwargs)
                    else:
                        return HttpResponse('You are not authorized')
        return wrapper_func
    return decorator