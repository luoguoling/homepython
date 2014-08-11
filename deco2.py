__author__ = 'Administrator'
def _auth(args):
    def __auth(func):
        def _login(request):
            username = request.session.get('login_user',False)
            if not username:
                return login(request)
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return login(request)
            if user.auth_group in (args or auth()) or (user.auth_group == 'admin')
                return func(request)
        return denied(request)
        return _login
    return __auth
