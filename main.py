import asyncio

from aiohttp import web

#from aiohttp_session import session_middleware
#from aiohttp_session import get_session
#from aiohttp_session.cookie_storage import EncryptedCookieStorage

#from datetime import datetime, timedelta

import logging
from routes import routes

from settings import SECRET_KEY
from settings import USERS_DB

log = logging.getLogger()
log.level = logging.INFO
logger_handler = logging.FileHandler('app.log')
logger_handler.setLevel(logging.INFO)
log.addHandler(logger_handler)

loop = asyncio.get_event_loop()

app = web.Application(loop=loop, middlewares=[
    #session_middleware(EncryptedCookieStorage(SECRET_KEY)),
    #authorize,
    #db_handler,
])

#adding routes
for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])

if __name__ == '__main__':
    web.run_app(app, port=8088)
