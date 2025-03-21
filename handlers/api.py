import requests

service_role_id = '5d74f8e4-8b2f-400f-93f2-1d2e973f2a02'

def apiclient(url:str, method:str, payload, params=None):
    params = params if params else {}
    return requests.request(
        method,
        data=payload,
        url=f"http://localhost:9000/v1/{url}",
        headers={
            "Content-Type": "application/json",
            "Authorization" : service_role_id
        },
        **params
    )