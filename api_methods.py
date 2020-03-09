from aiohttp import web
#from aiohttp_session import get_session
from db import Clients
from auxiliary import check_token, clientStats


async def findClient(request:web.Request):
    #session = await get_session(self.request)
    params_dict = await request.post()
    #search_queries = {
    #    k:params_dict[k]
    #    for k in params_dict 
    #    if (k in searchStats)}
    token = params_dict.get('token', '')
    if check_token(token)[0]:
        #ахтунг, при пустом запросе оно возвращает всех клиентов
        clients = Clients.select()\
            .where(
                Clients.phone.contains(params_dict.get('phone', '')),
                Clients.first_name.contains(params_dict.get('first_name', '')),
                Clients.last_name.contains(params_dict.get('last_name', '')),
                Clients.mid_name.contains(params_dict.get('mid_name', ''))
            )
        response = [
            {
                prop: str(getattr(i, prop)) for prop in clientStats
            } for i in clients
        ]
    else:
        response = {
            'error': 'invalid token',
            'token': token
        }
    #logging.info(response)
    return web.json_response(response)

async def getClientsInfo(request: web.Request):
    params = await request.post()
    ids = params.get('clients', '').split(',')
    token = params.get('token', '')
    if check_token(token)[0]:
        clients = Clients.select()\
            .where(
                Clients.id.in_(ids)
            )
        response = [
            {
                prop: str(getattr(i, prop)) for prop in clientStats
            } for i in clients
        ]
    else:
        response = {
            'error': 'invalid token',
            'token': token
        }
    #logging.info(response)
    return web.json_response(response)

# when a user logs in we want to increment their login count:
#User.update(login_count=User.login_count + 1).where(User.id == user_id)

async def setClientVisit(request: web.Request):
    params = await request.post()
    id_ = params.get('id', '')
    token = params.get('token', '')
    if check_token(token)[1]:
        ticket = Clients.select(Clients.ticket_workouts, Clients.ticket_expired)\
            .where(Clients.id == id_)
        for ticks in ticket:
            workouts = ticks.ticket_workouts
        if workouts > 0:
            Clients.update(ticket_workouts=Clients.ticket_workouts - 1)\
                .where(Clients.id == id_)
            response = {
                'status': True,
                'ticket_workouts': workouts - 1
            }
        else:
            response = {
                'error': 'client have no workouts',
                'id'   : id_
            }
    else:
        response = {
            'error': 'invalid token',
            'token': token
        }
    #logging.info(response)
    return web.json_response(response)

async def addClient(request: web.Request):
    pass

async def editClient(request: web.Request):
    pass

