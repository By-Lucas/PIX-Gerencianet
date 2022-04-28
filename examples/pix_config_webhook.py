from gerencianet import Gerencianet
from credentials import CREDENTIALS


gn = Gerencianet(CREDENTIALS)

headers = {
    'x-skip-mtls-checking': 'false'
}

params = {
    'chave': ''
}

body = {
    'webhookUrl': ''
}

response =  gn.pix_config_webhook(params=params, body=body, headers=headers)
print(response)
