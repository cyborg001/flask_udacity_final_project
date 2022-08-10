import requests

def predictions():
    data = {
    "CHAS":{
        "0":0
    },
    "RM":{
        "0":6.575
    },
    "TAX":{
        "0":296.0
    },
    "PTRATIO":{
        "0":15.3
    },
    "B":{
        "0":396.9
    },
    "LSTAT":{
        "0":4.98
    }
    }

    PORT=443
    PORT=5000

    cabeceras = {'Content-Type': 'application/json'} 
    # r = requests.post(f'https://calm-forest-cdeb821ed6704dc19dd91c6e1388512b.azurewebsites.net:{PORT}/predict', headers=cabeceras, 
    #             json=data)
    r = requests.post(f'127.0.0.1:{PORT}/predict', headers=cabeceras, 
                json=data)
    return r.json()
