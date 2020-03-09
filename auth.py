from aiohttp import web
from aiohttp_session import get_session

from peewee import SqliteDatabase
from db import db

class Login(web.View):

    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            url = self.request.app.router['main'].url()
            raise web.HTTPFound(url)
        return b'Please enter login or email'


class SignIn(web.View):

    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            url = self.request.app.router['main'].url()
            raise web.HTTPFound(url)
        return b'Please enter login or email'


class SignOut(web.View):

    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            url = self.request.app.router['main'].url()
            raise web.HTTPFound(url)
        return b'Please enter login or email'