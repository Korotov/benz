from api_methods import findClient, addClient, editClient, getClientsInfo, setClientVisit

routes = [
    ('POST', '/api/findClient',     findClient,     'findClient'),
    ('POST', '/api/addClient',      addClient,      'addClient'),
    ('POST', '/api/editClient',     editClient,     'editClient'),
    ('POST', '/api/getClientsInfo', getClientsInfo, 'getClientsInfo'),
    ('POST', '/api/setClientVisit', setClientVisit, 'setClientVisit'),
]