from handlers.api import apiclient
from handlers.api import service_role_id
import json

class crud_executor:
    def __init__(self, action, payload):
        self.service_role_id = service_role_id
        self.action = action
        self.payload = payload
    def exec(self):
        if self.action.startswith('rfq'):
            return self.rfq(self.payload, self.action.split(":")[1]).execute()
        elif self.action.startswith('quote'):
            return self.quote(self.payload, self.action.split(":")[1]).execute()
    
    class rfq:
        def __init__(self, payload, action):
            self.service_role_id = service_role_id
            self.action = action
            self.payload = payload
        def execute(self):
            if self.action == 'create':
                # self.payload[""]
                self.rfq_crud = rfq_crud(self.payload)
                return self.rfq_crud.create()
            elif ["update", "accept", "reject"].index(self.action) != -1:
                if self.action == 'accept':
                    self.payload["status"] = "accepted"
                if self.action == 'reject':
                    self.payload["status"] = "rejected"
                self.rfq_crud = rfq_crud(self.payload)
                return self.rfq_crud.status_update()
    class quote:
        def __init__(self, payload, action):
            self.service_role_id = service_role_id
            self.action = action
            self.payload = payload
        def execute(self):
            if self.action == 'create':
                self.quote_crud = quote_crud(self.payload)
                return self.quote_crud.create()
            elif ["update", "accept", "reject"].index(self.action):
                if self.action == 'accept':
                    self.payload["status"] = "accepted"
                if self.action == 'reject':
                    self.payload["status"] = "rejected"
                self.quote_crud = quote_crud(self.payload)
                return self.quote_crud.status_update()

class rfq_crud:
    def __init__(self, payload):
        self.service_role_id = service_role_id
        self.payload = payload
    def create(self):
        req_url = 'quotes/rfq'
        return apiclient(req_url, 'POST', json.dumps(self.payload))
    def status_update(self):
        req_url = f'quotes/rfq/{self.id}'
        return apiclient(req_url, 'POST', json.dumps(self.payload))
    
class quote_crud:
    def __init__(self, payload):
        self.service_role_id = service_role_id
        self.payload = payload
    def create(self):
        req_url = 'quotes'
        return apiclient(req_url, 'POST', json.dumps(self.payload))
    def status_update(self):
        req_url = f'quotes/rfq/{self.payload["id"]}'
        return apiclient(req_url, 'POST', json.dumps(self.payload))