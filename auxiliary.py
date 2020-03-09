from db import Admins
from aiohttp import web

def check_token(token):
    access = False, False
    admin = Admins.select()\
        .where(Admins.token == token)\
        .execute()
    try:
        admin = admin[0]
    except IndexError:
        pass
    else:
        access = admin.read_access, admin.write_access
    return access

class token_cheking():
    def __init__(self, read=None, write=None, **kwargs):
        self.read = read
        self.write = write
        self.params = kwargs
    async def __call__(self, func):
        async def wrapped(request: web.Request):
            post = request.post()
            params = {}
            token = params.get('token', '')
            for param in self.params:
                param = post.get(param, None)
                if not self.params[param] and param is None:
                    return web.json_response({
                        'error': 'invalid arguments, have no {} parameter'.format(param)
                    })
                else:
                    params[param] = post[param]
            access = check_token(token)
            if (isinstance(self.read, bool) and access[0]) or (isinstance(self.write, bool) and access[1]):
                return func(**params)
            else:
                return web.json_response({
                'error': 'permission denied'
            })
        return await wrapped

clientStats = (
    'id',
    'first_name',
    'last_name',
    'mid_name',
    'phone',
    'ticket_expired',
    'ticket_workouts')

searchStats = (
    'phone', 'first_name', 'last_name', 'mid_name'
    )